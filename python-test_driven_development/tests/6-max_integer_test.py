#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Clase de pruebas para la función max_integer"""

    def test_normal_list(self):
        """Prueba con una lista normal de números"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Prueba con una lista vacía"""
        self.assertIsNone(max_integer([]))

    def test_float_list(self):
        """Prueba con una lista de números flotantes"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5]), -1.5)

    def test_mixed_list(self):
        """Prueba con una lista mixta de enteros y flotantes"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([-1, -2.5, -3, -4.5]), -1)

    def test_duplicate_values(self):
        """Prueba con valores duplicados"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)

    def test_negative_values(self):
        """Prueba con valores negativos"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_single_value(self):
        """Prueba con un solo valor"""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([0]), 0)

    def test_no_argument(self):
        """Prueba sin argumentos"""
        self.assertIsNone(max_integer())

    def test_tuple_input(self):
        """Prueba con una tupla como entrada"""
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer((1, 3, 4, 2)), 4)

    def test_invalid_input(self):
        """Prueba con entradas inválidas"""
        with self.assertRaises(TypeError):
            max_integer("string")
        with self.assertRaises(TypeError):
            max_integer(123)
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            max_integer([1, 2, None, 4])


if __name__ == '__main__':
    unittest.main() 