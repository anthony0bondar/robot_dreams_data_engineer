from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


default_args = {
    "owner": "airflow",
    "email": ["airflow@airflow.com"],
    "email_ob_failure": False
}


dag = DAG(
    dag_id="spark_test",
    description="DAG with dynamic tasks",
    schedule_interval="@daily",
    start_date=datetime(2021, 5, 19),
    default_args=default_args
)

dummy1 = DummyOperator(
    task_id="dummy_1",
    dag=dag
)

'''
One more way to run spark job
'''
test = BashOperator(
    task_id="test_task_spark"
    , dag=dag
    , bash_command="spark-submit --name some_job  --jars /home/user/shared_folder/postgresql-42.2.20.jar --driver-class-path /home/user/shared_folder/postgresql-42.2.20.jar /home/user/shared_folder/spark.py"
)

dummy2 = DummyOperator(
    task_id="dummy_2",
    dag=dag
)

dummy1 >> test >> dummy2