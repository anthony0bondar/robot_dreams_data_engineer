# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets/iot-stream/data-device/

# COMMAND ----------

df = spark.read.json("/databricks-datasets/iot-stream/data-device/part-00000.json.gz")
display(df)

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE tmp.rules(
# MAGIC   user_gender varchar(2),
# MAGIC   age_less_than int,
# MAGIC   age_greater_than int,
# MAGIC   weight_less_than int,
# MAGIC   weight_greater_than int,
# MAGIC   user_is_smoker varchar(2),
# MAGIC   km_walked_greater_than int
# MAGIC );
# MAGIC 
# MAGIC INSERT into tmp.rules VALUES ('M', NULL, 52, NULL, 178, 'N', 2);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tmp.rules

# COMMAND ----------

# MAGIC %md
# MAGIC # Start

# COMMAND ----------

import pyspark.sql.functions as F

from pyspark.sql.types import StructType

# COMMAND ----------

batch_df = spark.read.json("/databricks-datasets/iot-stream/data-device/part-00000.json.gz")
schema = [i for i in batch_df.schema]
json_schema = StructType(schema)

# COMMAND ----------

device_data = spark.readStream\
  .schema(json_schema)\
  .option("maxFilesPerTrigger", 30)\
  .json("/databricks-datasets/iot-stream/data-device/")

# COMMAND ----------

user_df = spark.table("tmp.user")

# COMMAND ----------

device_data_pr = device_data.where(F.col('num_steps') >= 2000)
device_data_pr = device_data_pr\
  .withColumn('miles_walked', F.round(F.col('miles_walked') * 1.6, 3))\
  .withColumnRenamed('miles_walked', 'km_walked')

# COMMAND ----------

enriched_df = device_data_pr.join(user_df, device_data_pr.user_id == user_df.userid, 'inner')\
  .select(
    device_data_pr.device_id,
    device_data_pr.km_walked,
    device_data_pr.user_id,
    device_data_pr.timestamp,
    user_df.age,
    user_df.gender,
    user_df.weight,
    user_df.smoker
)

# COMMAND ----------

rules_df = spark.table("tmp.rules")

# COMMAND ----------

cond = [
  (enriched_df.gender == rules_df.user_gender)
  & ((enriched_df.age > rules_df.age_greater_than) | (enriched_df.age < rules_df.age_less_than))
  & ((enriched_df.weight > rules_df.weight_greater_than) | (enriched_df.weight < rules_df.weight_less_than))
  & (enriched_df.smoker == rules_df.user_is_smoker)
  & (enriched_df.km_walked > rules_df.km_walked_greater_than)
]

notifications = enriched_df.join(rules_df, cond)

# COMMAND ----------

users_notify = notifications.select('user_id', 'device_id', 'km_walked', 'timestamp')

# COMMAND ----------

users_notify.writeStream\
  .format('delta')\
  .outputMode('append')\
  .option("checkpointLocation", "/tmp/tmp/checkpoint")\
  .start("/tmp/tmp/16_delta_stream")

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE tmp.users_notify
# MAGIC USING DELTA
# MAGIC LOCATION '/tmp/tmp/16_delta_stream'

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tmp.users_notify

# COMMAND ----------

