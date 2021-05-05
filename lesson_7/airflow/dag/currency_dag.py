import requests
import json
import os

from datetime import datetime
from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def currency(**kwargs):
    BASE_URL = "https://api.ratesapi.io/api/latest"
    base_currencies = ['EUR', 'USD', 'PLN', 'GBP']
    os.makedirs(os.path.join('home', 'user', 'data', str(kwargs['execution_date'])), exist_ok=True)
    for base in base_currencies:

        query = {"base": base}
        response = requests.get(BASE_URL, params=query)

        response.raise_for_status()

        with open(os.path.join('home', 'user', 'data', str(kwargs['execution_date']), f'currencies_{base}.json'), 'w') as f:
            json.dump(response.json(), f)


default_args = {
    'owner': 'airflow',
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'retries': 2
}


dag = DAG(
    'currency_dag',
    schedule_interval='@daily',
    start_date=datetime(2021, 4, 26, 13),
    default_args=default_args
)

t1 = PythonOperator(
    task_id='currency_function',
    dag=dag,
    python_callable=currency,
    provide_context=True
)


