from gendiff.formaters.change_value import change_value


def string_convert(data, depth):
    if not isinstance(data, dict):
        return data
    lines = ['{']
    for key, value in data.items():
        lines.append(
            f"\n{'  ' * depth}  {key}: {string_convert(value, depth+2)}"
        )
    lines.append(f"\n{'  ' * (depth-1)}}}")
    return ''.join(lines)


def build_stylish(data, depth=1):
    STATS = {'unchanged': '  ',
             'added': '+ ',
             'removed': '- '}
    lines = []
    data = change_value(data)
    for key, value in data.items():
        if value['status'] == 'changed':
            lines.append(f"{'  ' * depth}- {key}: "
                         f"{string_convert(value['old'], depth+2)}\n")
            lines.append(f"{'  ' * depth}+ {key}: "
                         f"{string_convert(value['new'], depth+2)}\n")
        elif value['status'] == 'nested':
            lines.append(f"{'  ' * depth}  {key}: {{\n")
            lines.append(f"{build_stylish(value['value'], depth+2)}")
            lines.append(f"{'  ' * (depth+1)}}}\n")
        else:
            lines.append(f"{'  ' * depth}{STATS[value['status']]}{key}: "
                         f"{string_convert(value['value'], depth+2)}\n")
    return ''.join(lines)


def use_format(data):
    result = build_stylish(data)
    return f"{{\n{result}}}"
