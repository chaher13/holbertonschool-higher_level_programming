#!/usr/bin/python3
"""A function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Args:
        my_obj (object): The Python object to be converted to JSON.

    Returns:
        str: A JSON-formatted string representing the given object.
    """
    return json.dumps(my_obj)
