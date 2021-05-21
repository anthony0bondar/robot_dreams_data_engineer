import os
import logging

import pyspark
from pyspark.sql import SparkSession
from airflow.hooks.base_hook import BaseHook


def load_to_bronze(table):

    connection = BaseHook.get_connection("oltp_postgres")
    pg_creds = {
        'host': connection.host
        , 'port': connection.port
        , 'database': 'postgres'
        , 'user': connection.login
        , 'password': connection.password
    }

    spark = SparkSession.builder \
        .config('spark.driver.extraClassPath', '/home/user/shared_folder/postgresql-42.2.20.jar') \
        .config('spark.jars', '/home/user/shared_folder/postgresql-42.2.20.jar') \
        .master('local') \
        .appName("lesson") \
        .getOrCreate()

    df = spark.read.jdbc("jdbc:postgresql://127.0.0.1:5432/postgres"
                         , table=table
                         , properties={"user": "pguser", "password": "secret", "driver": "org.postgresql.Driver"})

    df.write.parquet(f"/bronze/{table}", mode="overwrite")
    logging.info("table saved to bronze")


if __name__ == '__main__':
    load_to_bronze('staff')
