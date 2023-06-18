#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor and returns the result
    as a new matrix.

    Args:
    matrix (list): The matrix to be divided, represented as a list of lists.
    Each inner list represents a row of the matrix.
    The elements of the matrix can be integers or floats.
    div (int, float): The divisor.

    Returns:
    list: A new matrix with the elements divided by the divisor. The elements
    are rounded to 2 decimal places.

    Raises:
    TypeError: If the matrix is not a matrix (list of lists)
    of integers/floats or if the divisor is not a number.
    ZeroDivisionError: If the divisor is zero.
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of\
        integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of\
            integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")

    if len(row) != len(matrix[0]):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round((i / div), 2))
        new_matrix.append(new_row)

    return new_matrix
