#!/usr/bin/python3
# 2-square.py
"""create a square class and check its arrtibutes"""


class Square:
    """create a new class Square"""

    def __init__(self, size=0):
        """initialize a new instance with its size set to zero
        Args:
            size (int): set to zero as default
        Return:
            raise TypeError if size is not int
            raiseValue error if size is less than zero
        """
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square to a new value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """function to return area of square"""

        return (self.__size)**2
