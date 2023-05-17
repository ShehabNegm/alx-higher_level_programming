#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function to return a matrix but its numbers are squared"""

    if matrix:
        new_matrix = []
        for i in matrix:
            new_matrix.append(list(map(lambda x: int(x**2), i)))
        return new_matrix
