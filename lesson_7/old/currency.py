import requests
import json
import os

BASE_URL = "https://api.ratesapi.io/api/latest"


def run():
    base_currencies = ['EUR', 'USD', 'RUB', 'PLN', 'GBP']
    result_list = []
    for base in base_currencies:
        query = {"base": base}
        response = requests.get(BASE_URL, params=query)

        if response.status_code != 200:
            raise Exception
        else:
            result_list.append(response.json())

        with open(os.path.join(os.getcwd(), 'data', 'currencies.json'), 'w') as f:
            json.dump(result_list, f)


if __name__ == '__main__':
    run()
