#!/usr/bin/python3
"""A method that creates a copy of a list"""


def copy_list(a_list):
    """
    Create a copy of a list.

    The function creates a new list that is a copy of the provided list.
    It uses list slicing to create the copy,
    which ensures that the original list remains unchanged.

    Args:
        a_list (list): The list to be copied.

    Returns:
        list: A new list that is a copy of the provided list.
    """
    return a_list[:]
