from datetime import datetime

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
    description='Sample DAG',
    schedule_interval='@hourly',
    start_date=datetime(2021,2,14,1,15),
    default_args=default_args
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
    depends_on_past=False
)

t3 = BashOperator(
    task_id='print_date2',
    bash_command='date',
    dag=dag
)

t1 >> t2 >> t3