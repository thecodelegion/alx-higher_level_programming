#!/usr/bin/python3

"""
Defines a function called `lookup` that takes an object as an argument
and returns a list of all available attributes of that object.
"""


def lookup(obj):
    """
    Returns a list of an object's available attributes.
    """
    # dir() returns a sorted list of attributes for the object.
    return dir(obj)
