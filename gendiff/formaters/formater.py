from gendiff.formaters import stylish, plain, json


FORMATERS = {'stylish': stylish,
             'plain': plain,
             'json': json}


def formater(data, format):
    return FORMATERS[format].use_format(data)
