#!/usr/bin/python3
"""
A function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Load JSON data from a file and convert it to a Python object.

    Args:
        filename (str): The name of the file to load JSON data from.

    Returns:
        object: A Python object representing the parsed JSON data.
    """
    with open(filename, 'r') as file:
        return json.load(file)
