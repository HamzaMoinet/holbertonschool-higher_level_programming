#!/usr/bin/env python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    :param data: Dictionary to be serialized
    :param filename: Name of the JSON file
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads data from a JSON file and deserializes it into a Python dictionary.

    :param filename: Name of the JSON file
    :return: Deserialized dictionary
    """
    with open(filename, 'r') as file:
        return json.load(file)

