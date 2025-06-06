#!/usr/bin/python3
"""Module for creating Python objects from JSON files."""

import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python data structure represented by the JSON file.

    Note:
        - Uses 'with' statement for file handling.
        - Does not handle file or JSON parsing exceptions.
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
