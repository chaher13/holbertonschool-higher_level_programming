#!/usr/bin/python3
""" This Class stands for a Rectangle """


class Rectangle:
    """
    This class represents a rectangle.

    Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.

    Methods:
    __init__(width=0, height=0): Initializes a new instance of\
    the Rectangle class.
    width(): Getter method for the width attribute.
    width(value): Setter method for the width attribute.
    height(): Getter method for the height attribute.
    height(value): Setter method for the height attribute.
    area(): Calculates the area of the rectangle.
    perimeter(): Calculates the perimeter of the rectangle.
    __str__(): Returns a string representation of the rectangle.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        width (int): The width of the rectangle. Default is 0.
        height (int): The height of the rectangle. Default is 0.

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
        value (int): The width of the rectangle.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle.

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
        value (int): The height of the rectangle.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        If width or height is 0, returns an empty string.
        Otherwise, returns a string representation
        of the rectangle using '#' characters.

        Returns:
        str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle object.

        Returns:
            str: A string representation of the rectangle object.
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when the rectangle object is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2
