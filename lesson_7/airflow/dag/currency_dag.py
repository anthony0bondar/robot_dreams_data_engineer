from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from currency_for_airflow import currency



default_args = {
    'owner': 'airflow',
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'retries': 2
}

dag = DAG(
    'currency_dag',
    description='currency dag',
    schedule_interval='@daily',
    start_date=datetime(2021,2,23,1,0),
    default_args=default_args
)

t1 = PythonOperator(
    task_id='currency_function',
    dag=dag,
    python_callable=currency
)

import pandas
from zipfile import ZipFile
from boto3.session import Session
session=Session()
s3 = session.resource('s3')
b = s3.Bucket()