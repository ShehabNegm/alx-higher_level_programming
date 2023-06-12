#!/usr/bin/python3
"""define class square from class rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define class square"""

    def __init__(self, size):
        """function to initilate square class"""

        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)
