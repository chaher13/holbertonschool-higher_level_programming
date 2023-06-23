#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Write text to a file.

    Args:
    filename (str): The name of the file to write to.
    If no filename is provided, an empty string is used.
    text (str): The text to write to the file.
    If no text is provided, an empty string is used.

    Returns:
    None
    """
    with open(filename, 'w') as f:
        f.write(text)
    return len(text)
