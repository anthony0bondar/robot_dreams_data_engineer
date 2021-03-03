from datetime import datetime

from airflow import DAG
from airflow.operators.http_operator import SimpleHttpOperator


default_args = {
    'owner': 'airflow',
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'retries': 2
}

dag = DAG(
    'currency_http_dag',
    description='currency http dag',
    schedule_interval='@daily',
    start_date=datetime(2021,2,23,1,0),
    default_args=default_args
)

t1 = SimpleHttpOperator(
    task_id='get_data_via_http',
    http_conn_id='http_default',
    endpoint='?base=GBP',
    method='GET',
    xcom_push=True,
    dag=dag
)
