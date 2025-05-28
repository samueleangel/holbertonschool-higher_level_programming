#!/usr/bin/python3
"""
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """
        Raises an Exception to indicate that the area method is not imp..
        """
        raise Exception("area() is not implemented")
