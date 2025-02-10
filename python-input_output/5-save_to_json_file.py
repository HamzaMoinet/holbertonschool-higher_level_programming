#!/usr/bin/python3
"""Save Object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """save json file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
