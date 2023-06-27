#!/usr/bin/python3
""" class Base"""


import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
        list_dictionaries (list): List of dictionaries.

        Returns:
        str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
        cls (class): The class itself.
        list_objs (list): List of instances to be saved.

        Returns:
        None.
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by the JSON string.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set based\
        on the provided dictionary.

        Args:
            dictionary (dict): Dictionary containing the attribute-value pairs\
        for the instance.

        Returns:
            object: Instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file in JSON format.

        Returns:
        list: List of instances loaded from the file.
        If the file doesn't exist, returns an empty list.
        """
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                data = file.read()
                instance_list = cls.from_json_string(data)
                instances = []
                for instance in instance_list:
                    instances.append(cls.create(**instance))
                return instances
        else:
            return []
