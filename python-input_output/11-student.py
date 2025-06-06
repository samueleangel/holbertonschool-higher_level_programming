#!/usr/bin/python3
"""Module for Student class with serialization/deserialization."""

class Student:
    """Class representing a student with JSON serialization/deserialization."""

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
        """Retrieve a dictionary representation of the Student.
        Args:
            attrs (list): Optional list of attribute names to include
        Returns:
            dict: Dictionary containing student attributes
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) 
                   for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.
        Args:
            json (dict): Dictionary of attributes to replace
        """
        for key, value in json.items():
            setattr(self, key, value)
