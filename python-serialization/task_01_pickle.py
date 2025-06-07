#!/usr/bin/env python3
"""Custom object serialization using pickle."""

import pickle

class CustomObject:
    """Custom class for pickle serialization demo."""
    
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize object to file using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize object from file."""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
