#!/usr/bin/python3
"""define subclass"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle from basegeometery"""

    def __init__(self, width, height):
        """instantion function"""

        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
