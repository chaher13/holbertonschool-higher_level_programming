#!/usr/bin/python3
"""
  This class represents a square.

  Attributes:
    __size (int): The size of the square.

  Methods:
    __init__(size): Initializes a new instance of the Square class.

"""


class Square:
    """
    Initializes a new instance of the Square class.

      Args:
          size (int): The size of the square. Default is 0.

      Raises:
          TypeError: If size is not an integer.
          ValueError: If size is less than 0.
    """
    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
