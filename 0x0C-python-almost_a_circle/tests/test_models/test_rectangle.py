#!/usr/bin/python3
"""unittest for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    """class to test using unittest module"""

    def test_rec_base(self):
        """test rec instance"""
        self.assertIsInstance(Rectangle(3, 4), Base)

    def test_rec_no_arg(self):
        """test no args to rec"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rec_one_arg(self):
        """test one arg to rec"""
        with self.assertRaises(TypeError):
            Rectangle(13)

    def test_more_rec_args(self):
        """test more args to rec than defined"""
        with self.assertRaises(TypeError):
            Rectangle(1, 5, 6, 7, 8, 10)

    def test_rec_width_private(self):
        """test private attribute width"""
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 45, 4, 6, 1).__width)

    def test_rec_height_private(self):
        """test private attribute height"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1).__height)

    def test_rec_x_private(self):
        """test private attribute x"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1).__x)

    def test_rec_y_private(self):
        """test private attribute y"""
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 1, 1, 1).__y)

    def test_rec_id_empty(self):
        """test class rectangle with none id"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_rec_id_assigned(self):
        """test class rectangle with assigned id"""
        r = Rectangle(1, 1, 1, 1, 7)
        self.assertEqual(r.id, 7)

    def test_rec_id_mixed(self):
        """test class rectangle with mixed ids"""
        r1 = Rectangle(4, 6)
        r2 = Rectangle(10, 12)
        r3 = Rectangle(2, 1, 0, 0, 128)
        r4 = Rectangle(12, 24)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 128)
        self.assertEqual(r1.id, r4.id - 2)

    def test_rec_width_getter(self):
        """test class rectangle width arrtibute"""
        r = Rectangle(3, 4)
        r1 = Rectangle(12, 24, 0, 1)
        r2 = Rectangle(1, 1, 1, 1, 0)
        self.assertEqual(r.width, 3)
        self.assertEqual(r1.width, 12)
        self.assertEqual(r2.width, 1)

    def test_rec_height_getter(self):
        """test class rectangle height"""
        r1 = Rectangle(7, 8)
        r2 = Rectangle(8, 9)
        r3 = Rectangle(1, 1, 1, 1, 12)
        r4 = Rectangle(3, 5, 0, 0)
        self.assertEqual(r1.height, 8)
        self.assertEqual(r2.height, 9)
        self.assertEqual(r3.height, 1)
        self.assertEqual(r4.height, 5)

    def test_rec_x_getter(self):
        """test class rectangle x"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 12)
        r3 = Rectangle(1, 1, 0, 0)
        r4 = Rectangle(5, 6, 70, 24, 69)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 12)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r4.x, 70)

    def test_rec_y_getter(self):
        """test class retangle y"""
        r1 = Rectangle(3, 4)
        r2 = Rectangle(3, 4, 5)
        r3 = Rectangle(3, 4, 9, 10)
        r4 = Rectangle(3, 4, 9, 1, 89)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 10)
        self.assertEqual(r4.y, 1)

    def test_rec_width_setter(self):
        """test rec width setter"""
        r = Rectangle(1, 2)
        r.width = 12
        self.assertEqual(r.width, 12)

    def test_rec_height_setter(self):
        """test rec height setter"""
        r = Rectangle(3, 4)
        r.height = 66
        self.assertEqual(r.height, 66)

    def test_rec_x_setter(self):
        """test rec x setter"""
        r = Rectangle(12, 15, 13)
        r.x = 0
        self.assertEqual(r.x, 0)

    def test_rec_y_setter(self):
        """test rec y setter"""
        r = Rectangle(10, 4, 5, 6)
        r.y = 99
        self.assertEqual(r.y, 99)

    def test_rec_id_setter(self):
        """test rec id setter"""
        r = Rectangle(1, 2, 3, 4)
        r.id = 177
        self.assertEqual(r.id, 177)


class testRectangle_width(unittest.TestCase):
    """class to unittest rectangle width"""

    def test_width_normal(self):
        """test rec width"""
        r = Rectangle(1, 2)
        r.width = 3
        self.assertEqual(r.width, 3)

    def test_width_zero(self):
        """test rec width zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 12)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 12)

    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("lol", 12)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.2, 4)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2], 1)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2), 13)

    def test_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({}, 1)

    def test_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(12), 7)

    def test_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 7)

    def test_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 8)

    def test_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 17)

    def test_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3, 4}, 6)
