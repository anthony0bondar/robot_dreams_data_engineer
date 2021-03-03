import requests
import json
import os

from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator

from httpnew import ComplexHttpOperator


def currency():
    BASE_URL = "https://api.ratesapi.io/api/latest"
    base_currencies = ['EUR', 'USD', 'RUB', 'PLN', 'GBP']
    res = []

    for base in base_currencies:

        query = {
            "base": base
        }

        response = requests.get(BASE_URL, params=query)

        if response.status_code != 200:
            raise Exception
        else:
            res.append(response.json())
        print(response.json())

    with open(os.path.join(os.getcwd(), 'data', 'result.json'), 'w') as f:
        json.dump(res, f)


default_args = {
    "owner": "airflow",

    "depends_on_past": False,
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    'end_date': datetime(9999, 1, 1),
}


dag = DAG(
    'currencies_dag',
    description='Retrieving currencies from API',
    schedule_interval='@daily',
    start_date=datetime(2021, 2, 14, 1, 15),
    default_args=default_args
)

# run_this = PythonOperator(
#     task_id='currency_function',
#     python_callable=currency,
#     dag=dag,
# )

run_this2 = ComplexHttpOperator(
    task_id='currency_http_op',
    http_conn_id='http_default',
    endpoint='',
    method='GET',
    data={"base": "GBP"},
    xcom_push=False, 
    dag=dag,
    save_flag=True

)