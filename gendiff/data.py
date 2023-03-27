import json
import yaml
import os


formats = {'json': json.load,
           'yml': yaml.safe_load,
           'yaml': yaml.safe_load}


def prepare_dict(data, format):
    if format not in formats:
        raise ValueError(f'Unsupported file format. Supported formats: '
                         f'{", ".join(list(formats.keys()))}')
    return formats[format](data)


def read_data(path):
    return open(path)


def get_format(file):
    return os.path.splitext(file)[1].lstrip('.')
