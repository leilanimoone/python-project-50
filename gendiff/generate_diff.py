from gendiff.data import prepare_data


def generate_diff(first_file, second_file):
    data1 = prepare_data(first_file)
    data2 = prepare_data(second_file)
    diff = str()
    sorted_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in sorted_keys:
        if key not in data1:
            diff += f'+ {key}: {data2[key]}\n'
        elif key not in data2:
            diff += f'- {key}: {data1[key]}\n'
        elif data1[key] == data2[key]:
            diff += f'  {key}: {data1[key]}\n'
        elif data1[key] != data2[key]:
            diff += f'- {key}: {data1[key]}\n'
            diff += f'+ {key}: {data2[key]}\n'
    return '{\n' + diff + '}'