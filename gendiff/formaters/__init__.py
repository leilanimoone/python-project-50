from . import stylish, plain, json


FORMATERS = {'stylish': stylish.build_stylish,
             'plain': plain.build_plain,
             'json': json.build_json}


def formater(data, format):
    return FORMATERS[format](data)
