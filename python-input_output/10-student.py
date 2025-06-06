#!/usr/bin/python3
"""Module for defining a Student class with filtered JSON serialization."""


class Student:
    """Class representing a student with filtered JSON conversion."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a filtered dictionary representation of the Student.

        Args:
            attrs (list): Optional list of attribute names to include

        Returns:
            dict: Dictionary containing requested student attributes
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) 
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__
