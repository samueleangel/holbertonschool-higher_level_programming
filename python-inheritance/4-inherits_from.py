#!/usr/bin/python3
"""
Function that checks if an object is an instance of a class
that inherits (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherits (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check inheritance against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
