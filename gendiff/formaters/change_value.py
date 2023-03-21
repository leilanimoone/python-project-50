def change_value(data):
    correct_value = {True: 'true',
                     False: 'false',
                     None: 'null'}

    for key, value in data.items():
        if isinstance(value, dict):
            change_value(value)
        elif isinstance(value, (bool, type(None))):
            data[key] = correct_value[value]
    return data
