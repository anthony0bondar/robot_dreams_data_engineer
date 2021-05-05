from datetime import datetime

from airflow import DAG

import json
import os

from airflow.exceptions import AirflowException
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.hooks.http_hook import HttpHook


class ComplexHttpOperator(SimpleHttpOperator):

    def __init__(self, save_path, *args, **kwargs):
        super(ComplexHttpOperator, self).__init__(*args, **kwargs)
        self.save_path = save_path

    def execute(self, context):
        http = HttpHook(self.method, http_conn_id=self.http_conn_id)

        self.log.info("Calling HTTP method")

        response = http.run(self.endpoint,
                            self.data,
                            self.headers,
                            self.extra_options)
        if self.log_response:
            self.log.info(response.text)
        if self.response_check:
            if not self.response_check(response):
                raise AirflowException("Response check returned False.")
        if self.save_path:
            if not os.path.exists(os.path.dirname(self.save_path)):
                try:
                    os.makedirs(os.path.dirname(self.save_path))
                except OSError:
                    raise OSError
            self.log.info('Saving response to %s path', self.save_path)
            with open(self.save_path, 'w') as f:
                json.dump(response.json(), f)
        if self.xcom_push_flag:
            return response.text


default_args = {
    'owner': 'airflow',
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'retries': 0
}

dag = DAG(
    'currency_complexhttp_dag',
    description='currency complex http dag',
    schedule_interval='@daily',
    start_date=datetime(2021,4,25,1,0),
    default_args=default_args
)

t1 = ComplexHttpOperator(
    task_id='get_data_via_http',
    http_conn_id='currencies',
    endpoint='?base=GBP',
    method='GET',
    save_path='/home/user/data/data/currencies.json',
    xcom_push=True,
    dag=dag
)




