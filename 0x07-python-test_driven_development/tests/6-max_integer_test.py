#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class to test using unittest module"""

    def test_max_integer(self):
        """function to test function max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 10, 4, 6]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 5]), 5)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -5, -2, -10]), -1)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([7]), 7)
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))
