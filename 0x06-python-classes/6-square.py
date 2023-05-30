#!/usr/bin/python3
# 2-square.py
"""create a square class and check its arrtibutes"""


class Square:
    """create a new class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new instance with its size set to zero
        Args:
            size (int): set to zero as default
        Return:
            raise TypeError if size is not int
            raiseValue error if size is less than zero
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of square to a new value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the value of a position)"""

        if (not isinstance(value, tuple) or
                value[0] < 0 or
                value[1] < 0 or
                len(value) != 2 or
                type(value[0]) != int or
                type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """function to return area of square"""
        return (self.__size)**2

    def my_print(self):
        """function to print a square"""
        i = self.__size
        poX = self.__position[0]
        poY = self.__position[1]

        if i == 0:
            print()
            return

        for row in range(poY):
            print()

        for k in range(i):
            for col in range(poX):
                print(" ", end="")
            for j in range(i):
                print("#", end="")
            print()
