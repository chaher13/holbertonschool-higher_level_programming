#!/usr/bin/python3
"""Write a class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write an class Square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[square] {self.__size}/{self.__size}"
