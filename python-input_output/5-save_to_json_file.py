#!/usr/bin/python3
"""
A function that writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Save a Python object to a JSON file.

    Args:
        my_obj (object): The Python object to be saved as JSON.
        filename (str): The name of the file to save the JSON data to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
