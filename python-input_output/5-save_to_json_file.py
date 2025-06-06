#!/usr/bin/python3
"""Module for saving Python objects to files in JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Args:
        my_obj: Python object to be serialized.
        filename (str): Name of the file to write to.

    Note:
        - Uses 'with' statement for file handling.
        - Does not handle serialization or permission exceptions.
        - Overwrites existing file content.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
