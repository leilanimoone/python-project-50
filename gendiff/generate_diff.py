from gendiff.data import prepare_dict, get_format, read_data
from gendiff.get_diff import get_diff
from gendiff.formaters import formater


def generate_diff(file1, file2, format_name='stylish'):
    data1 = prepare_dict(read_data(file1), get_format(file1))
    data2 = prepare_dict(read_data(file2), get_format(file2))
    diff = get_diff(data1, data2)
    return formater(diff, format_name)
