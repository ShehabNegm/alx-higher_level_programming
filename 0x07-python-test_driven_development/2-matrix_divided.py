#!/usr/bin/python3
# 2-matrix_divided.py
""" will define a function to divide a matrix"""


def matrix_divided(matrix, div):
    """function to divid matrix by a div

    Args:
        matrix  (list of list of ints) : matrix to be divided
        div (int ot float) : will divide matrix, if zero raise error

    Return:
        a new divided matrix
    """

    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for row in matrix:

        if type(row) is not list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda j: list(map(lambda k: round((k / div), 2), j)),
                    matrix))
