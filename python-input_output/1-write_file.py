#!/usr/bin/python3
"""Module for writing a string to a file and returning the character count."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns the number of chars..

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The string to write to the file. Defaults to "".

    Returns:
        int: The number of characters written.

    Note:
        - Creates the file if it doesn't exist.
        - Overwrites existing content.
        - Uses 'with' statement for automatic file handling.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
