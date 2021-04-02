import os
import json


def write_json():
    py_dict = {"this": "is", "python": "dict"}
    with open(file=os.path.join('.', 'data', 'sample_json.json'), mode='w') as json_file:
        json.dump(py_dict, json_file)


def read_json():
    with open(file=os.path.join('.', 'data', 'sample_json.json'), mode='r') as json_file:
        py_dict = json.load(json_file)
    print(py_dict)


if __name__ == '__main__':
    write_json()
    read_json()
