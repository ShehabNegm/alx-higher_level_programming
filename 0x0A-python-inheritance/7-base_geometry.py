#!/usr/bin/python3
# 7-base_geometry.py
"""class base_geometry definition"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """function to return area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to check value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
