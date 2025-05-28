#!/usr/bin/python3
"""
Module that contains the function is_kind_of_class which checks
if an object is an instance of a specified class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or a subclass of that class.

    Args:
        obj (any): The object to check.
        a_class (type): The class or superclass to check against.

    Returns:
        bool: True if obj is an instance of a_class or its subclasses..
    """
    return isinstance(obj, a_class)
