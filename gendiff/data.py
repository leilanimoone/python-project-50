import json
import yaml
import os


formats = {'json': json.load,
           'yml': yaml.safe_load,
           'yaml': yaml.safe_load}


def prepare_data(file, format):
    with open(file) as data:
        return formats[format](data)


def get_format(file):
    return os.path.splitext(file)[1].lstrip('.')
