#!/usr/bin/python3
"""
Function that returns the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of the given object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: Sorted list of strings with attributes and method names.
    """
    return sorted(dir(obj))
