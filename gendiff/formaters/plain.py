from gendiff.formaters.change_value import change_value


def string_convert(data):
    values = ('true', 'false', 'null')
    if isinstance(data, dict):
        return '[complex value]'
    elif data in values or isinstance(data, (int, float)):
        return data
    else:
        return f"'{data}'"


def build_plain(data, path=''):
    lines = []
    data = change_value(data)
    for key in data:
        full_path = f"{path}{key}"
        res = data[key]
        if res['status'] == 'added':
            lines.append(f"Property '{full_path}' "
                         f"was added with value: "
                         f"{string_convert(res['value'])}")
        elif res['status'] == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif res['status'] == 'changed':
            lines.append(f"Property '{full_path}' was updated. "
                         f"From {string_convert(res['old'])} to "
                         f"{string_convert(res['new'])}")
        elif res['status'] == 'nested':
            p = build_plain(res['value'], f"{full_path}.")
            lines.append(f"{p}")
    return '\n'.join(lines)


def use_format(data):
    return build_plain(data)
