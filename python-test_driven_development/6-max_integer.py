#!/usr/bin/python3
"""Módulo para encontrar el entero máximo en una lista"""

def max_integer(list=[]):
    """Función que encuentra y retorna el entero máximo en una lista de enteros.
    Si la lista está vacía, retorna None.
    """
    if not isinstance(list, (list, tuple)):
        raise TypeError("list must be a list of integers or floats")
    if len(list) == 0:
        return None
    result = list[0]
    for i in range(1, len(list)):
        if list[i] > result:
            result = list[i]
    return result 