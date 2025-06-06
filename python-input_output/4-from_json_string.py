#!/usr/bin/python3
"""Module for converting JSON strings to Python objects."""

import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: Python data structure represented by the JSON string.

    Note:
        Does not handle JSON decode exceptions (per requirements).
    """
    return json.loads(my_str)
