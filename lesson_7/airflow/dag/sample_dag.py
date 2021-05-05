from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'retries': 2
}

dag = DAG(
    'sample_dag',
    description='1st Sample Dag',
    schedule_interval='@hourly',
    start_date=datetime(2021, 4, 27, 13),
    default_args= default_args
)

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=dag,
    retries=3,
    retry_delay=timedelta(minutes=1)
)

t3 = BashOperator(
    task_id='print_date_2',
    bash_command='date',
    dag=dag
)

t1 >> t2 >> t3