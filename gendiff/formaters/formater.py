from gendiff.formaters import stylish


FORMATERS = {'stylish': stylish}


def formater(data, format):
    return FORMATERS[format].use_format(data)
