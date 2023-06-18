#!/usr/bin/python3
"""unittest for Rectangle class"""

import unittest
from io import StringIO
from unittest.mock import patch
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


class testRectangle_height(unittest.TestCase):
    """class to test rec height"""

    def test_height_normal(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -10)

    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "WTF")

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 0.7)

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, [])

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, (1, 3))

    def test_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"a": 1, "b": 2})

    def test_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(8))

    def test_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, False)

    def test_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('inf'))

    def test_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, float('nan'))

    def test_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {1, 2, 3})


class testRectangle_x(unittest.TestCase):
    """class to unittest rectangle x"""

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -5)

    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, None)

    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, "test")

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 6, 0.99)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 12, [])

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (8, 9))

    def test_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, {"a": 1, "b": 2})

    def test_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 5, range(1))

    def test_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True)

    def test_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 9, float('inf'))

    def test_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 9, float('nan'))

    def test_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 6, {2, 4})

    def test_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(6, 9, complex(8))


class testRectangle_y(unittest.TestCase):
    """class to test rec y"""

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -5)

    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 6, None)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "ALX!")

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 0.1)

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, [])

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 9, 10, (8, 9))

    def test_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 7, 10, {"a": 2})

    def test_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(12, 2, 0, range(1))

    def test_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, False)

    def test_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, float('inf'))

    def test_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 4, float('nan'))

    def test_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {1, 2})

    def test_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(2))


class testRectangle_ErrorPriority(unittest.TestCase):
    """class to test error printing priority"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("lol", "lol2")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("lol", 2, "X")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("lol", 2, 3, "y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "x", "y")


class testRectangle_area(unittest.TestCase):
    """class to test area method of the rectangle"""

    def test_area_normal(self):
        r = Rectangle(2, 4)
        self.assertEqual(r.area(), 8)

    def test_area_x(self):
        r = Rectangle(4, 5, 6)
        self.assertEqual(r.area(), 20)

    def test_area_y(self):
        r = Rectangle(1, 1, 1, 4)
        self.assertEqual(r.area(), 1)

    def test_area_id(self):
        r = Rectangle(2, 2, 2, 2, 17)
        self.assertEqual(r.area(), 4)

    def test_area_changeArg(self):
        r = Rectangle(2, 6)
        r.width = 12
        r.height = 10
        self.assertEqual(r.area(), 120)

    def test_area_error(self):
        r = Rectangle(12, 10)
        with self.assertRaises(TypeError):
            r.area(7)


class testRectangle_display(unittest.TestCase):
    """class to test display() class method"""

    def test_rec_display_one(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(1, 1)
            r.display()
            self.assertEqual(f.getvalue(), '#\n')

    def test_rec_display_sqr(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(2, 2, 0, 0, 12)
            r.display()
            self.assertEqual(f.getvalue(), '##\n##\n')

    def test_rec_display_rec(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(3, 4)
            r.display()
            self.assertEqual(f.getvalue(), '###\n###\n###\n###\n')

    def test_rec_display_error(self):
        r = Rectangle(2, 3, 0, 0, 12)
        with self.assertRaises(TypeError):
            r.display(2)

    def test_rec_display_x(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(2, 3, 1)
            r.display()
            self.assertEqual(f.getvalue(), ' ##\n ##\n ##\n')

    def test_rec_display_xy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(2, 3, 1, 1)
            r.display()
            self.assertEqual(f.getvalue(), '\n ##\n ##\n ##\n')


class testRectangle_str(unittest.TestCase):
    """class to test __str__ method of the class"""

    def test_rec_str_normal(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r = Rectangle(4, 6, 2, 1, 1)
            print(r)
            self.assertEqual(f.getvalue().strip(), '[Rectangle] (1) 2/1 - 4/6')

    def test_rec_str_x(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Rectangle(4, 6, 2)
            print(r1)
            output = "[Rectangle] ({}) 2/0 - 4/6".format(r1.id)
            self.assertEqual(f.getvalue().strip(), output)

    def test_rec_str(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Rectangle(4, 6)
            print(r1)
            output = "[Rectangle] ({}) 0/0 - 4/6".format(r1.id)
            self.assertEqual(f.getvalue().strip(), output)


class testRectangle_update(unittest.TestCase):
    """class to test update() class method"""

    def test_rec_update_empty(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update()
            print(r1)
            output = "[Rectangle] ({}) 10/10 - 10/10".format(r1.id)
            self.assertEqual(f.getvalue().strip(), output)

    def test_rec_update_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(69)
            print(r1)
            output = "[Rectangle] (69) 10/10 - 10/10"
            self.assertEqual(f.getvalue().strip(), output)

    def test_rec_update_width(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89, 2)
            print(r1)
            output = "[Rectangle] (89) 10/10 - 2/10"
            self.assertEqual(f.getvalue().strip(), output)

    def test_rec_update_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(89, 2, 3, 4, 5, 7)
            print(r1)
            output = "[Rectangle] (89) 4/5 - 2/3"
            self.assertEqual(f.getvalue().strip(), output)
