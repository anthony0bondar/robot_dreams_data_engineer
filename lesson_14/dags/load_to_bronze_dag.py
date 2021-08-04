import os
import yaml

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

from functions.load_to_bronze import load_to_bronze, load_to_bronze_spark


default_args = {
    "owner": "airflow",
    "email_on_failure": False
}


def return_tables():
    return ('film', 'film_actor','actor','category','film_category','language')


def load_to_bronze_group(value):
    return PythonOperator(
        task_id="load_"+value+"_to_bronze",
        python_callable=load_to_bronze_spark,
        op_kwargs={"table": value}
    )


dag = DAG(
    dag_id="load_to_bronze",
    description="Load data from PostgreSQL data base to Data Lake bronze",
    schedule_interval="@daily",
    start_date=datetime(2021, 8, 2),
    default_args=default_args
)

dummy1 = DummyOperator(
    task_id='start_load_to_bronze',
    dag=dag
)
dummy2 = DummyOperator(
    task_id='finish_load_to_bronze',
    dag=dag
)

for table in return_tables():
    dummy1 >> load_to_bronze_group(table) >> dummy2
