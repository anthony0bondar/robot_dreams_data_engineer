from datetime import datetime

from airflow import DAG
from complexhttp import ComplexHttpOperator


default_args = {
    'owner': 'airflow',
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'retries': 2
}

dag = DAG(
    'currency_complexhttp_dag',
    description='currency complex http dag',
    schedule_interval='@daily',
    start_date=datetime(2021,2,22,1,0),
    default_args=default_args
)

t1 = ComplexHttpOperator(
    task_id='get_data_via_http',
    http_conn_id='http_default',
    endpoint='?base=GBP',
    method='GET',
    save_path='/usr/local/airflow/data/currencies.json',
    xcom_push=True,
    dag=dag
)
