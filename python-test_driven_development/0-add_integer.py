#!/usr/bin/python3
"""
Módulo que contiene una función para sumar dos números enteros.
"""


def add_integer(a, b=98):
    """
    Suma dos números enteros.

    Args:
        a: Primer número (entero o flotante)
        b: Segundo número (entero o flotante), por defecto 98

    Returns:
        La suma de a y b como entero

    Raises:
        TypeError: Si a o b no son enteros o flotantes
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer ")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer ")

    return int(a) + int(b)
