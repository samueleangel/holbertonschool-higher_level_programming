#!/usr/bin/python3
"""
Módulo que contiene una función para imprimir texto con indentación.
"""


def text_indentation(text):
    """
    Imprime un texto con 2 líneas nuevas después de cada '.', '?' y ':'.

    Args:
        text: Texto a imprimir (string)

    Raises:
        TypeError: Si text no es un string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ['.', '?', ':']:
            result += '\n\n'

    print(result.strip()) 