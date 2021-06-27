import requests
import json
import os

from datetime import date

from requests.exceptions import HTTPError

from config import Config


def app(config, process_date=None):

    if not process_date:
        process_date = str(date.today())

    os.makedirs(os.path.join(config['directory'], process_date), exist_ok=True)

    try:
        for currency in config['symbols']:

            url = config['url'] + '/' + process_date
            params = {'access_key': config['access_key'], 'symbols': currency}

            response = requests.get(url, params=params)
            response.raise_for_status()

            with open(os.path.join(config['directory'], process_date, currency+'.json'), 'w') as json_file:
                data = response.json()
                data = data['rates']
                json.dump(data, json_file)

    except HTTPError:
        print('Error!')


if __name__ == '__main__':
    config = Config(os.path.join('.', 'config.yaml'))
    date = ['2021-06-24', '2021-06-19', '2021-06-20', '2021-06-21']
    for dt in date:
        app(
            config=config.get_config('currency_app')
            , process_date=dt
        )
