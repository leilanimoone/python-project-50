def get_diff(data1, data2):  # noqa: C901
    diff = []
    sorted_keys = sorted(list(set(data1.keys()) | set(data2.keys())))
    for key in sorted_keys:
        if key not in data1:
            diff.append({'key': key,
                         'status': 'added',
                         'value': data2[key]})
        elif key not in data2:
            diff.append({'key': key,
                         'status': 'removed',
                         'value': data1[key]})
        elif isinstance(data1[key], dict) & isinstance(data2[key], dict):
            child = get_diff(data1[key], data2[key])
            diff.append({'key': key,
                        'status': 'nested',
                         'value': child})
        elif data1[key] == data2[key]:
            diff.append({'key': key,
                         'status': 'unchanged',
                         'value': data1[key]})
        elif data1[key] != data2[key]:
            diff.append({'key': key,
                         'status': 'changed',
                         'old': data1[key],
                         'new': data2[key]})
    return diff
