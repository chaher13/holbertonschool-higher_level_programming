#!/usr/bin/python3
"""
This function takes an object as input and returns the list of attributes
 and methods of that object.
"""


def lookup(obj):
    """
    Parameters:
        obj : object
        The object to inspect.

    Returns:
    list
    A sorted list of attribute and method names of the object.
    """
    return dir(obj)
