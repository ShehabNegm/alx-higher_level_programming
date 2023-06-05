#!/usr/bin/python3
"""define a new class"""


class Rectangle:
    """new class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a new instance of class Rectangle
        Args:
            width (int) : width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """function to return the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """function to return the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """function to print rectangle"""
        if self.__height == 0 or self.__width == 0:
            return("")

        L = []
        for h in range(self.__height):
            [L.append(str(self.print_symbol)) for w in range(self.__width)]
            if h != self.__height - 1:
                L.append("\n")
        return ("".join(L))

    def __repr__(self):
        """return string represntation of class"""
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """print message on deleting class instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
