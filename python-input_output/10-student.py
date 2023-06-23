#!/usr/bin/python3
"""A class Student that defines a student """


class Student:
    """
    A class representing a student.

    The Student class has attributes for first name, last name, and age.
    It provides a method, to_json(), that converts
    the student object to a dictionary representation.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the student object to a dictionary representation.

        Args:
        attrs (list): Optional. A list of attribute names
        to include in the dictionary.
        If not provided, all attributes will be included.

        Returns:
        dict: A dictionary containing the student's information.
        The keys are the attribute names, and the values are the corresponding
        attribute values.
        If 'attrs' is provided, only the specified attributes will be included.
        """
        if attrs is None:
            return self.__dict__
        info_student = {}
        for i in attrs:
            if i in self.__dict__:
                info_student[i] = self.__dict__[i]
        return info_student
