from gendiff.data import prepare_data, get_format
from gendiff.get_diff import get_diff
from gendiff.formaters.formater import formater


def generate_diff(file1, file2, format='stylish'):
    data1 = prepare_data(file1, get_format(file1))
    data2 = prepare_data(file2, get_format(file2))
    diff = get_diff(data1, data2)
    return formater(diff, format)
