#!/usr/bin/python3
"""Module for appending text to a file and returning character count."""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file and returns chars added.

    Args:
        filename (str): File to append to. Defaults to "".
        text (str): Text to append. Defaults to "".

    Returns:
        int: Number of characters appended.

    Note:
        - Creates file if it doesn't exist.
        - Uses 'with' statement for proper file handling.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
