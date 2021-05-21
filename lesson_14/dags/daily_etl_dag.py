from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from functions.load_to_bronze import load_to_bronze

default_args = {
    "owner": "airflow",
    "email": ["airflow@airflow.com"],
    "email_ob_failure": False
}


def return_tables():
    return ['film', 'film_actor', 'actor', 'film_category', 'category', 'language']


def to_bronze_group(value):
    return PythonOperator(
        task_id="load_"+value+"_to_bronze",
        python_callable=load_to_bronze,
        op_kwargs={"table": value},
        dag=dag
    )

dag = DAG(
    dag_id="daily_etl",
    description="DAG with dynamic tasks",
    schedule_interval="@daily",
    start_date=datetime(2021, 5, 19),
    default_args=default_args
)

dummy2 = DummyOperator(
    task_id="dummy_2",
    dag=dag
)

for i in return_tables():
    to_bronze_group(i) >> dummy2