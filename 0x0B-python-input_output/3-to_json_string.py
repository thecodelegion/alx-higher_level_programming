#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a string object.

    Args:
        my_obj (str): The string object to convert to JSON.

    Returns:
        str: The JSON representation of the string object.
    """
    return json.dumps(my_obj)
