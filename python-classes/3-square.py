#!/usr/bin/python3
"""
    This class represents a square.

"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(size): Initializes a new instance of the Square class.
        area(): Calculates the area of the square.
    """

    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            return self.__size ** 2
