#!/usr/bin/python3
"""
A function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Convert a class object to a JSON-serializable dictionary.

    The function takes a class object as input and converts it to
    a dictionary that can be serialized as JSON.
    It iterates over the object's attributes and includes only
    the attributes of type list, dict, str, int, or bool.
    Other attribute types are excluded from the resulting dictionary.

    Args:
    obj (object): The class object to be converted
    to a JSON-serializable dictionary.

    Returns:
    dict: A dictionary representing the JSON-serializable
    attributes of the given object.
    """
    if isinstance(obj, type):
        raise TypeError("obj must be a class")

    final_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            final_dict[key] = value

    return final_dict
