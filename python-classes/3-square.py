#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.
        Args:
        size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns:
        The area of the square
        """
        return self.__size ** 2
