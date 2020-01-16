import json


def load_data(path):
    with open(path, 'r') as file:
        users_dict = json.load(file)

    return users_dict
