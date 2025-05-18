#!/usr/bin/python3
"""
Módulo que contiene una función para imprimir un nombre.
"""


def say_my_name(first_name, last_name=""):
    """
    Imprime un nombre en el formato "My name is <first name> <last name>".

    Args:
        first_name: Primer nombre (string)
        last_name: Apellido (string), opcional

    Raises:
        TypeError: Si first_name o last_name no son strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}") 