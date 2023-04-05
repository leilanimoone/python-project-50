def to_string(data, depth):
    if isinstance(data, dict):
        lines = ['{']
        for key, value in data.items():
            if isinstance(value, dict):
                new_value = to_string(value, depth + 4)
                lines.append(f"{' ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * depth}    {key}: {value}")
        lines.append(f"{' ' * depth}}}")
        return '\n'.join(lines)
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return data


def build_stylish(data, depth=0):
    lines = ['{']
    for dictionary in data:
        key = dictionary['key']
        if dictionary['status'] == 'changed':
            old = to_string(dictionary['old'], depth + 4)
            new = to_string(dictionary['new'], depth + 4)
            lines.append(f"{' ' * depth}  - {key}: {old}")
            lines.append(f"{' ' * depth}  + {key}: {new}")
        elif dictionary['status'] == 'removed':
            value = to_string(dictionary['value'], depth + 4)
            lines.append(f"{' ' * depth}  - {key}: {value}")
        elif dictionary['status'] == 'nested':
            new_dict = build_stylish(dictionary['value'], depth + 4)
            lines.append(f"{' ' * depth}    {key}: {new_dict}")
        elif dictionary['status'] == 'added':
            value = to_string(dictionary['value'], depth + 4)
            lines.append(f"{' ' * depth}  + {key}: {value}")
        else:
            value = to_string(dictionary['value'], depth + 4)
            lines.append(f"{' ' * depth}    {key}: {value}")
    lines.append(f"{' ' * depth}}}")
    return '\n'.join(lines)
