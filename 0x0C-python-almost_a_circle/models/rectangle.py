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
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """get x position of rectangle printing"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """get y position of rectangle printing"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""

        return self.width * self.height

    def display(self):
        """print rectangle using # to stdout"""
        for y in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """function to print rectangle info to stdout"""

        return ("[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" +
                str(self.y) + " - " + str(self.width) + "/" + str(self.height))

    def update(self, *args, **kwargs):
        """class method that updates rectangle class using args"""
        L = list(args)

        if args and len(L) != 0:
            try:
                self.id = L[0]
                self.width = L[1]
                self.height = L[2]
                self.x = L[3]
                self.y = L[4]

            except IndexError:
                pass

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """return dictionary rep. of Rectangle class"""

        rec_dict = {"id": self.id, "width": self.width, "x": self.x,
                    "y": self.y, "height": self.height}

        return rec_dict
