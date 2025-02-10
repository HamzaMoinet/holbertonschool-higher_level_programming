#!/usr/bin/python3
"""Save Object to a file"""


import json


def load_from_json_file(filename):
    """save json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
