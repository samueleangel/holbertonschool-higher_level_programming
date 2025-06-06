#!/usr/bin/python3
"""Module for defining a Student class with JSON serialization capability."""


class Student:
    """Class representing a student with basic info and JSON conversion."""

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

    def to_json(self):
        """Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: Dictionary containing the student's attributes
        """
        return self.__dict__
