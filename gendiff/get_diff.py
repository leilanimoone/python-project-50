def get_diff(data1, data2):  # noqa: C901
    diff = {}
    sorted_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in sorted_keys:
        if key not in data1:
            diff[key] = {'status': 'added',
                         'value': data2[key]}
        elif key not in data2:
            diff[key] = {'status': 'removed',
                         'value': data1[key]}
        elif isinstance(data1[key], dict) & isinstance(data2[key], dict):
            child = get_diff(data1[key], data2[key])
            diff[key] = {'status': 'nested',
                         'value': child}
        elif data1[key] == data2[key]:
            diff[key] = {'status': 'unchanged',
                         'value': data1[key]}
        elif data1[key] != data2[key]:
            diff[key] = {'status': 'changed',
                         'old': data1[key],
                         'new': data2[key]}
    return diff
