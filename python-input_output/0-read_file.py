#!/usr/bin/python3
"""Module for reading and printing the contents of a text file."""


def read_file(filename=""):
    """Reads a UTF-8 encoded text file and prints its contents to stdout.

    This function opens the specified file in read mode with UTF-8 encoding,
    reads its entire content, and prints it to standard output. The file is
    automatically closed after reading, thanks to the `with` statement.

    Args:
        filename (str, optional): The path to the file to be read.

    Note:
        - The function does not handle file permission  exceptions.
        - No external modules are imported, as per requirements.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
