#!/usr/bin/python3


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If the size is not an integer or a non-negative float.
        ValueError: If the size is a negative integer.

    Example:
        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####
    """

    if not (isinstance(size, int)) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
