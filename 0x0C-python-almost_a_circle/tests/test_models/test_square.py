#!/usr/bin/python3
"""unittest for Square class"""

import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare(unittest.TestCase):

    def test_sqr_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_sqr_rec(self):
        self.assertIsInstance(Square(2), Rectangle)

    def test_sqr_no_arg(self):
        with self.assertRaises(TypeError):
            Square()

    def test_sqr_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(3, 1, 3)
        self.assertEqual(s2.area(), 9)
        s3 = Square(4, 1, 3, 12)
        self.assertEqual(s3.area(), 16)

    def test_sqr_display(self):
        with patch('sys.stdout', new=StringIO()) as f:
            s = Square(2, 2, 1)
            s.display()
            self.assertEqual(f.getvalue(), '\n  ##\n  ##\n')

    def test_sqr_printing(self):
        with patch('sys.stdout', new=StringIO()) as f:
            s1 = Square(5)
            print(s1)
            output = "[Square] ({}) 0/0 - 5".format(s1.id)
            self.assertEqual(f.getvalue().strip(), output)

    def test_sqr_size_setter(self):
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_sqr_size_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("10")

    def test_sqr_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            s1 = Square(5)
            s1.update(1, 2, 3, 4)
            print(s1)
            output = "[Square] (1) 3/4 - 2"
            self.assertEqual(f.getvalue().strip(), output)
