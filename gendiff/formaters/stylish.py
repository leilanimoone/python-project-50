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
    if isinstance(data, type(None)):
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return data


def stylish_format(data, depth=0):
    lines = ['{']
    for dictionary in data:
        if dictionary['status'] == 'changed':
            lines.append(f"{' ' * depth}  - {dictionary['key']}: "
                         f"{to_string(dictionary['old'], depth + 4)}")
            lines.append(f"{' ' * depth}  + {dictionary['key']}: "
                         f"{to_string(dictionary['new'], depth + 4)}")
        elif dictionary['status'] == 'removed':
            lines.append(f"{' ' * depth}  - {dictionary['key']}: "
                         f"{to_string(dictionary['value'], depth + 4)}")
        elif dictionary['status'] == 'nested':
            new_dict = stylish_format(dictionary['value'], depth + 4)
            lines.append(f"{' ' * depth}  "
                         f"  {dictionary['key']}: {new_dict}")
        elif dictionary['status'] == 'added':
            lines.append(f"{' ' * depth}  + {dictionary['key']}: "
                         f"{to_string(dictionary['value'], depth + 4)}")
        else:
            lines.append(f"{' ' * depth}    {dictionary['key']}: "
                         f"{to_string(dictionary['value'], depth + 4)}")
    lines.append(f"{' ' * depth}}}")
    return '\n'.join(lines)
