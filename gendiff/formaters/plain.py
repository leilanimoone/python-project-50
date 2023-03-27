def to_string(data):
    if isinstance(data, bool):
        return str(data).lower()
    if isinstance(data, dict):
        return '[complex value]'
    if isinstance(data, (int, float)):
        return data
    if isinstance(data, type(None)):
        return 'null'
    return f"'{data}'"


def plain_format(data, path=''):
    lines = []
    for dictionary in data:
        full_path = f"{path}{dictionary['key']}"
        if dictionary['status'] == 'added':
            lines.append(f"Property '{full_path}' "
                         f"was added with value: "
                         f"{to_string(dictionary['value'])}")
        elif dictionary['status'] == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif dictionary['status'] == 'changed':
            lines.append(f"Property '{full_path}' was updated. "
                         f"From {to_string(dictionary['old'])} to "
                         f"{to_string(dictionary['new'])}")
        elif dictionary['status'] == 'nested':
            p = plain_format(dictionary['value'], f"{full_path}.")
            lines.append(f"{p}")
    return '\n'.join(lines)
