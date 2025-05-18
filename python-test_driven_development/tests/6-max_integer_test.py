#!/usr/bin/python3
"""
Unittest para max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Prueba con una lista regular"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Prueba con una lista vacía"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Prueba con números negativos"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_numbers(self):
        """Prueba con números flotantes"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_single_element(self):
        """Prueba con un solo elemento"""
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_numbers(self):
        """Prueba con números duplicados"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_mixed_numbers(self):
        """Prueba con números mixtos"""
        self.assertEqual(max_integer([1, -2, 3.5, 0]), 3.5)

    def test_string_input(self):
        """Prueba con entrada de string"""
        with self.assertRaises(TypeError):
            max_integer("string")

    def test_none_input(self):
        """Prueba con entrada None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_types(self):
        """Prueba con tipos mixtos"""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3]) 