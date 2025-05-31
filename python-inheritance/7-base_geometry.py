#!/usr/bin/python3
"""
Module to validate integer values for geometry.
"""


class BaseGeometry:
    """
    Base class for working with geometric shapes.
    """

    def area(self):
        """
        This method just raises an exception because it’s not implemented yet.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Checks that a value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to check.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is zero or less.
        """
        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
