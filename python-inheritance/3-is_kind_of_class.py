#!/usr/bin/python3
"""
a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the given object is an instance
    or subclass of the specified class

    Parameters:
        obj : object
            The object to check.
        a_class : class
            The class to compare against.

    Returns:
        bool
        True if the object is an instance or subclass of the specified class
        False otherwise.
    """
    return isinstance(obj, a_class)
