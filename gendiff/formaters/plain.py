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


def build_plain(data, begin_path=''):
    lines = []
    for node in data:
        path = f"{begin_path}{node['key']}"
        if node['status'] == 'added':
            value = to_string(node['value'])
            lines.append(f"Property '{path}' was added with value: {value}")
        elif node['status'] == 'removed':
            lines.append(f"Property '{path}' was removed")
        elif node['status'] == 'changed':
            old = to_string(node['old'])
            new = to_string(node['new'])
            lines.append(f"Property '{path}' was updated. From {old} to {new}")
        elif node['status'] == 'nested':
            full_path = build_plain(node['value'], f"{path}.")
            lines.append(f"{full_path}")
    return '\n'.join(lines)
