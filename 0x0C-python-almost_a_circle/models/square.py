#!/usr/bin/python3
# square.py
"""define class square that inherets from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class square initialization"""

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size"""
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """function to ptint represntation of square"""

        return ("[Square] " + "(" + str(self.id) + ") "
                + str(self.x) + "/" + str(self.y)
                + " - " + str(self.size))

    def update(self, *args, **kwargs):
        """class method that updates square class using args, kwargs"""

        L = list(args)

        if args and len(L) != 0:
            try:
                self.id = L[0]
                self.size = L[1]
                self.x = L[2]
                self.y = L[3]

            except IndexError:
                pass

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
