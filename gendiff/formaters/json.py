import json
from gendiff.formaters.change_value import change_value


def use_format(data):
    data = change_value(data)
    return json.dumps(data, indent=4)
