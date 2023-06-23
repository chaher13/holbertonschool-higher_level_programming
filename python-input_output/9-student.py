#!/user/bin/python3
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

    def to_json(self):
        """
        Convert the student object to a dictionary representation.

        Returns:
            dict: A dictionary containing the student's information.
                  The keys are 'first_name', 'last_name', and 'age'.
        """
        info_student = {'first_name': self.first_name,
                        'last_name': self.last_name,
                        'age': self.age}
        return info_student
