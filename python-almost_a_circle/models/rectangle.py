#!/usr/bin/python3
""" Rectangle Class inheriting from the Base class"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle. Default is 0.
            y (int, optional): y-coordinate of the rectangle. Default is 0.
            id (int, optional): Identifier of the rectangle. Default is None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the width is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the height is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): The new x-coordinate of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If x is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): The new y-coordinate of the rectangle.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If y is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the Rectangle instance.

        Returns:
        The area of the Rectangle, which is calculated by multiplying the width
        by the height.

        Example:
        r = Rectangle(3, 4)
        print(r.area())  # Output: 12
        """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle instance using the character '#' to represent each
        cell of the rectangle. The number of '#' printed will correspond to the
        width and height of the rectangle.
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Format: "[Rectangle] (id) x/y - width/height"

        Returns:
        str: The string representation of the Rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} -\
 {self.width}/{self.height}"

    def update(self, *args):
        """
        Update the attributes of the Rectangle object with\
        the provided arguments.

        Args:
        *args: The arguments to update the attributes.
        The order should be as follows:
               1st argument -> id attribute
               2nd argument -> width attribute
               3rd argument -> height attribute
               4th argument -> x attribute
               5th argument -> y attribute
        """
        attr = ["id", "width", "height", "x", "y"]

        for i, arg in enumerate(args):
            setattr(self, attr[i], arg)
