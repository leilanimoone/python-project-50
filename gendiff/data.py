import json


def prepare_data(file):
    with open(file, 'r') as data:
        return json.load(data)
