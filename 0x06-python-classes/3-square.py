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

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """function to return area of square"""

        return (self.__size)**2
