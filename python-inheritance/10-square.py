#!/usr/bin/python3
"""A class Square"""


class Square(Rectangle):
    """A class representing a square.

    The Square class inherits from the Rectangle class
    and represents a square shape.
    It inherits all the attributes and methods from the Rectangle class.

    Attributes:
        __size (int): The length of each side of the square.

    Methods:
        __init__(size): Initializes a new instance of the Square class.
    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The length of each side of the square.
        """
        super().__init__(size, size)
        self.__size = size
