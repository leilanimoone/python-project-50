from gendiff.formaters import stylish, plain


FORMATERS = {'stylish': stylish,
             'plain': plain}


def formater(data, format):
    return FORMATERS[format].use_format(data)
