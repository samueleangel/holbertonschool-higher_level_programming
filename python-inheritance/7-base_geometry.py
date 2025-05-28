#!/usr/bin/python3
"""
Defines the class BaseGeometry with area() and integer_validator() methods.
"""


class BaseGeometry:
    """
    BaseGeometry class with area and integer validation methods.
    """

    def area(self):
        """
        Placeholder method for area. Raises Exception by default.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): the name of the value.
            value (any): the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is <= 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
