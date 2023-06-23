#!/usr/bin/python3
"""
A script that adds all arguments to a Python list,
and then save them to a file
"""

import sys
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


def add_arguments_to_list_and_save():
    """
    Add command-line arguments to a Python list and save them to a JSON file.

    The script uses the 'load_from_json_file' function to load an existing list
    from the file 'add_item.json'.
    If the file doesn't exist, an empty list is created. Then, it adds
    all the command-line arguments to the list.
    Finally, it saves the updated list to the file using
    the 'save_to_json_file' function.

    Args:
        None

    Returns:
        None
    """

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []

    my_list.extend(sys.argv[1:])

    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    add_arguments_to_list_and_save()
