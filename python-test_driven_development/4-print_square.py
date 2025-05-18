#!/usr/bin/python3
"""
Módulo que contiene una función para imprimir un cuadrado.
"""


def print_square(size):
    """
    Imprime un cuadrado usando el carácter '#'.

    Args:
        size: Tamaño del cuadrado (entero)

    Raises:
        TypeError: Si size no es un entero
        ValueError: Si size es menor que 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size) 