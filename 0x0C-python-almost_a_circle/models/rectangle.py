#!/usr/bin/python3
# rectangle.py
"""define class rectangle"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class Retangle initialization"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""
        self.__height = value

    @property
    def x(self):
        """get x position of rectangle printing"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        self.__x = value

    @property
    def y(self):
        """get y position of retangle printing"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        self.__y = value
