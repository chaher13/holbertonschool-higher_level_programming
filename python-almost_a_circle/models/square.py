#!/usr/bin/python3
""" A Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape, inheriting from the Rectangle class.

    Attributes:
        size (int): The length of each side of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): An optional identifier for the square.

    Methods:
    __init__(self, size, x=0, y=0, id=None):
    Initializes a Square instance with the given size, position,
    and optional id

    __str__(self):
        Returns a string representation of the square in the format:
        "[Square] (id) x/y - width".
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance with the given size, position,
        and optional id.

        Args:
            size (int): The length of each side of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): An optional identifier for the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format "[Square] (id) x/y - width".
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square (width or height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size value for the square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.
        Args:
            *args: List of arguments.
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
            **kwargs: Dictionary of keyword arguments, where each key
                represents an attribute.
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square instance.
        Returns:
            dict: Dictionary representation of the Square instance.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
