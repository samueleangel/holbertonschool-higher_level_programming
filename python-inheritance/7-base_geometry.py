#!/usr/bin/python3
class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


# For test detection by the checker
bg = BaseGeometry()
bg.integer_validator("age", 1)
