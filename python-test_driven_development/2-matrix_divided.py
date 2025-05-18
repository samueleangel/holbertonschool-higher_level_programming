#!/usr/bin/python3
"""
Módulo que contiene una función para dividir todos los elementos de una matriz.
"""


def matrix_divided(matrix, div):
    """
    Divide todos los elementos de una matriz por un número.

    Args:
        matrix: Lista de listas de enteros o flotantes
        div: Número por el cual dividir (entero o flotante)

    Returns:
        Nueva matriz con los elementos divididos y redondeados a 2 decimales

    Raises:
        TypeError: Si matrix no es una matriz válida o div no es un número
        ZeroDivisionError: Si div es 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(x, (int, float)) for row in matrix for x in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number ")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix] 