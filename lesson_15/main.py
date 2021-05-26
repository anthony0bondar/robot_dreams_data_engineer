from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark import SparkContext
from functools import partial
from pyspark import StorageLevel


def main():
    spark = SparkSession.builder \
        .master('local') \
        .appName("lesson") \
        .getOrCreate()
    sc = spark.sparkContext

    # ----
    def my_squared(s):
        return s*s
    spark.udf.register("my_squared", my_squared)

    spark.range(1, 1000).createOrReplaceTempView("test")
    df = spark.table("test")

    spark.sql("""
            SELECT id, my_squared(id) FROM test
        """).show(999)
    df.select("id", my_squared(F.col("id"))).show()

    # ----
    emps = sc.parallelize([[1, 'Anton'],[2, 'Vasya'],[3, 'Kolya']]).toDF(("id", "name"))
    salary = sc.parallelize([[1, 2000],[2, 3500],[3, 4000]]).toDF(("emp_id", "salary"))

    emps.join(salary, emps.id==salary.emp_id).select('name', 'salary').explain()
    emps.join(F.broadcast(salary), emps.id==salary.emp_id).select('name', 'salary').explain()

    # ----
    def filter_non_42(item, accumulator):
        if item % 2 == 0:
            accumulator += 1
        return '42' in str(item)

    accumulator = sc.accumulator(0)
    counting_filter = partial(filter_non_42, accumulator=accumulator)
    print(sc.range(0,10000).filter(counting_filter).sum())
    print('accum', accumulator)
    print(accumulator.value)

    # ----
    film = spark.read.parquet('/silver/film')
    film.repartition(2, 'rating').explain()

    # ----
    actor = spark.read.parquet('/bronze/actor')
    film_actor = spark.read.parquet('/bronze/film_actor')

    actor.write.bucketBy(4, 'actor_id').sortBy('actor_id').saveAsTable("actor_bucketed", format="parquet", mode="overwrite")
    film_actor.write.bucketBy(4, 'actor_id').sortBy('actor_id').saveAsTable("film_actor_bucketed", format="parquet", mode="overwrite")

    # ----
    film = spark.read.parquet('/bronze/film')
    film = film.filter(F.col('film_id') < F.lit(750))

    film.persist(StorageLevel.MEMORY_ONLY)

    film_pg13 = film.filter(F.col('rating')==F.lit('PG-13'))
    film_r = film.filter(F.col('rating')==F.lit('R'))


if __name__ == '__main__':
    main()
