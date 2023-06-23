#!/usr/bin/python3
""" A function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """
    Read the contents of a file and print them.

    Args:
    filename (str): The name of the file to be read.
    If no filename is provided, an empty string is used.

    Raises:
        FileNotFoundError: If the specified file is not found.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    print(read_data)
