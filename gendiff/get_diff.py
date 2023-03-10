def is_bool(value):
    if str(value) == 'True':
        return 'true'
    elif str(value) == 'False':
        return 'false'
    else:
        return value


def get_diff(data1, data2):
    diff = str()
    sorted_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in sorted_keys:
        if key not in data1:
            diff += f'  + {key}: {is_bool(data2[key])}\n'
        elif key not in data2:
            diff += f'  - {key}: {is_bool(data1[key])}\n'
        elif data1[key] == data2[key]:
            diff += f'    {key}: {is_bool(data1[key])}\n'
        elif data1[key] != data2[key]:
            diff += f'  - {key}: {is_bool(data1[key])}\n'
            diff += f'  + {key}: {is_bool(data2[key])}\n'
    return '{\n' + diff + '}'
