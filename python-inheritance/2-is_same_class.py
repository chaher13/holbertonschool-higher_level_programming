#!/usr/bin/python3
"""
a function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object belongs to the specified class.

    Parameters:
        obj : object
            The object to check.
        a_class : class
            The class to compare against.

    Returns:
        bool
            True if the object is an instance of the specified class,
            False otherwise.
    """
    return type(obj) is a_class
