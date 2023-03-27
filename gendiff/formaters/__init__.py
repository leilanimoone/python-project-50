from . import stylish, plain, json


FORMATERS = {'stylish': stylish.stylish_format,
             'plain': plain.plain_format,
             'json': json.json_format}


def formater(data, format):
    return FORMATERS[format](data)
