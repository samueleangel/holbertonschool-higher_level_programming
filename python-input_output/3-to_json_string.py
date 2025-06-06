#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object as a string.

    Args:
        my_obj: Python object to be serialized to JSON.

    Returns:
        str: JSON string representation of the object.

    Note:
        Does not handle serialization exceptions (per requirements).
    """
    return json.dumps(my_obj)
