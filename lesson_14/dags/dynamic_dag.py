from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from functions.sample_python_func import sample_python_func

default_args = {
    "owner": "airflow",
    "email": ["airflow@airflow.com"],
    "email_ob_failure": False
}


def return_values():
    return ['film', 'film_actor', 'actor', 'film_category', 'category', 'language']


def group(value):
    return PythonOperator(
        task_id="load_"+value,
        python_callable=sample_python_func,
        op_kwargs={"var": value},
        dag=dag
    )


dag = DAG(
    dag_id = "sample_dynamic_dag",
    description = "DAG with dynamic tasks",
    schedule_interval = "@daily",
    start_date = datetime(2021, 5, 19),
    default_args=default_args
)

dummy1 = DummyOperator(
    task_id="dummy_1",
    dag=dag
)

dummy2 = DummyOperator(
    task_id="dummy_2",
    dag=dag
)

for i in return_values():
    dummy1 >> group(i) >> dummy2