from airflow.exceptions import AirflowException
from airflow.hooks.http_hook import HttpHook
from airflow.operators.http_operator import SimpleHttpOperator

import json
import os
import logging


class ComplexHttpOperator(SimpleHttpOperator):
    def __init__(self, save_flag, *args, **kwargs):
        super(ComplexHttpOperator, self).__init__(*args, **kwargs)
        self.save_flag = save_flag

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
        if self.xcom_push_flag:
            return response.text

        self.log.info('berfore saving')
        if self.save_flag:

            with open('/usr/local/airflow/data/result.json', 'w') as f:
                json.dump(response.json(), f)
                self.log.info('while saving')
            self.log.info('after saving')
