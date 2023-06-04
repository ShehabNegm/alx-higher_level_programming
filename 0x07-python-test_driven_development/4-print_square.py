#!/usr/bin/python3
# 4-print_square.py
""" define function to print a square"""


def print_square(size):
    """define function to print a square with size

    Args:
        size (int) : size of length of square must be int

    Return: will print square with size length
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0 and type(size) is not float:
        raise ValueError("size must be >= 0")

    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
