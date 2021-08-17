# Databricks notebook source
# MAGIC %fs
# MAGIC ls /databricks-datasets/iot-stream/data-user/

# COMMAND ----------

df = spark.read.json("/databricks-datasets/iot-stream/data-device/part-00000.json.gz")

# COMMAND ----------

user = spark.read.option("header", True).option("inferSchema", True).csv("/databricks-datasets/iot-stream/data-user/userData.csv")

user = user.select('userid', 'gender', 'age', 'weight', 'smoker')

# COMMAND ----------

user.write.format("delta").save("/tmp/tmp/16")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE tmp.user
# MAGIC USING DELTA
# MAGIC LOCATION '/tmp/tmp/16' 

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from tmp.user;

# COMMAND ----------

