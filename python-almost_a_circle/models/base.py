#!/usr/bin/python3
""" class Base"""


class Base:
    """
    Base class for managing id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of Base.

        Args:
            id (int): The id value for the instance (optional).

        Attributes:
            id (int): The id value of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
