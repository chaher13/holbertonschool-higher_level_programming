def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
    a (int, float): The first number.
    b (int, float): The second number. Default is 98.

    Returns:
    int: The sum of the two numbers as an integer.

    Raises:
    TypeError: If either `a` or `b` is not an integer or a float.
    """

    if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)) or b is None:
        raise TypeError("b must be an integer or a float")

    a = int(a)
    b = int(b)

    return a + b
