#!/usr/bin/python3
"""unittest for Base class file base.py"""


import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """class to test using unittest module"""
    
    def test_base_id_empty(self):
        """function to test base id empty"""

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_id_assigned(self):
        """function to test assigned id"""

        b = Base(20)
        self.assertEqual(b.id, 20)
        b.id = 17
        self.assertEqual(b.id, 17)

    def test_case_id_mixed(self):
        """function to test mixed id assignment"""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(69)
        b5 = Base(12)
        b6 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b4.id, 69)
        self.assertEqual(b5.id, 12)
        self.assertEqual(b1.id, b6.id - 3)

    def test_two_args(self):
        """test 2 arguments"""
        with self.assertRaises(TypeError):
            Base(12, 2)

    def test_id_str(self):
        """test id as string"""
        b_str = Base("shehab")
        self.assertEqual(b_str.id, "shehab")
