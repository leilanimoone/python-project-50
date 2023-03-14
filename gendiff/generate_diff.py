from gendiff.data import prepare_data
from gendiff.data import get_format
from gendiff.get_diff import get_diff


def generate_diff(file1, file2):
    data1 = prepare_data(file1, get_format(file1))
    data2 = prepare_data(file2, get_format(file2))
    return get_diff(data1, data2)
