#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON-formatted string to be converted
    to a Python object.

    Returns:
        object: A Python object representing the parsed JSON data.
    """
    return json.loads(my_str)
