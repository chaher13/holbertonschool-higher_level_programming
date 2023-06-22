#!/usr/bin/python3
"""
A class BaseGeometry
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    Methods:
    __init__():
        Initializes an instance of BaseGeometry.

    integer_validator(name, value):
        Validates if a given value is an integer greater than 0.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            int: The validated integer value.
    """

    def __init__(self):
        """
        Initializes an instance of BaseGeometry.
        """
        pass

    def integer_validator(self, name, value):
        """
        Validates if a given value is an integer greater than 0.

        Parameters:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        Returns:
            int: The validated integer value.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

        return value
