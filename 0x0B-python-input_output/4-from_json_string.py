#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to a Python data structure.

    Returns:
        Any: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
