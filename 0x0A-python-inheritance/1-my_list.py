#!/usr/bin/python3

"""
Custom list class `MyList` inherits from
the built-in `list` class.
"""


class MyList(list):
    """
    Custom list that inherits from the built-in `list` class.
    Adds a new method `print_sorted()` that can be used to print
    the contents of the list in sorted order.
    """

    def print_sorted(self):
        """
        Sorts the list in ascending order and then prints it.
        """
        print(sorted(self))
