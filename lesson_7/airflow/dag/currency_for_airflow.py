import requests
import json
import os


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

    with open(os.path.join(os.getcwd(), 'data', 'result.json'), 'w') as f:
        json.dump(res, f)
