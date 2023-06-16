#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """
    This class represents a square.
    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
        size (int): The size of the square. Default is 0.
        position (tuple): The position of the square. Default is (0, 0).

        Raises:
        TypeError: If size is not an integer or position is not a tuple of two\
        positive integers.
        ValueError: If size is less than 0 or positions are less than 0.
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square
        Returns:
        The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
        value (int): The size of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
        value (tuple): The position of the square.

        Raises:
        TypeError: If value is not a tuple of two positive integers.
        ValueError: If position coordinates are less than 0.
        """
        if (
                not isinstance(value, tuple) or len(value) != 2
                or not isinstance(value[0], int)
                or not isinstance(value[1], int)
                or value[0] < 0
                or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """
        Prints a representation of the square.
        If size is 0, prints a newline.
        Otherwise, prints a square with '#' characters,
        using the position attribute to specify indentation.

        Example:
            >>> square = Square(3, (2, 1))
            >>> square.my_print()
              ###
              ###
              ###
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
