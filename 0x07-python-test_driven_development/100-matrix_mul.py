#!/usr/bin/python3
# 100-matrix_mul.py
"""define function"""


def matrix_mul(m_a, m_b):
    """define function to multiply 2 matrixes

    Args:
        m_a (list of list) : matrix 1
        m_b /list of list) : matrix 2
    Return:
        will return new matrix m_a * m_b
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(m_a[0]) != len(row_a):
            raise TypeError("each row of m_a must be of the same size")
        for a in row_a:
            if type(a) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")

    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(m_b[0]) != len(row_b):
            raise TypeError("each row of m_b must be of the same size")
        for b in row_b:
            if type(b) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    col_a = len(m_a[0])
    row_b = len(m_b)

    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = ([[sum(i * j for i, j in zip(i_row, j_col))
                    for j_col in zip(*m_b)] for i_row in m_a])

    return new_matrix
