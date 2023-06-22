#!/usr/bin/python3
"""
A function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Checks if the given object is a subclass of the specified class.

    Parameters:
        obj : object
            The object to check.
        a_class : class
            The class to compare against.

    Returns:
        bool
            True if the object is a subclass of the specified class,
            False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
