#!/usr/bin/python3
"""
A custom list class that extends the built-in list class.
"""


class MyList(list):
    """
    Methods:
        __init__():
            Initializes an instance of MyList.

        print_sorted():
            Prints the elements of the list in sorted order.
    """

    def __init__(self):
        """
        Initializes an instance of MyList.
        """
        pass

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
