#!/usr/bin/python3

"""
This module contains
a function to work with numbers.

Function:
    -add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    adds two integers together.

    Parameters:
        a (int): The first number to add.
        b (int): The second number to add.

    Returns:
        int: the sum of the two integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
