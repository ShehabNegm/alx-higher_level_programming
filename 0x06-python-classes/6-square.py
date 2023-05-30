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

        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

        if (not isinstance(position, tuple) or
                position[0] < 0 or
                position[1] < 0 or
                len(position) > 2):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @property
    def position(self):
        """get position og the square"""
        return self.__position

    @size.setter
    def size(self, value):
        """set the size of square to a new value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """set the value of a position)"""
        self.__position = value

    def area(self):
        """function to return area of square"""
        return (self.__size)**2

    def my_print(self):
        """function to print a square"""
        i = self.__size
        poX = self.__position[0]
        poY = self.__position[1]

        for row in range(poY):
            print()

        if i == 0:
            print()
        else:
            for k in range(i):
                for col in range(poX):
                    print(" ", end="")
                for j in range(i):
                    print("#", end="")
                print()
