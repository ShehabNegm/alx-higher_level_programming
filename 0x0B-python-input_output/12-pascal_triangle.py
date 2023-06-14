#!/usr/bin/python3
"""representing the Pascal’s triangle"""


def pascal_triangle(n):
    """function to print pascal triangle

    arrgs:
        n (int) : n rows of triangle
    Return:
        list of list or empty list if n < = 0
    """

    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    else:
        tri = [[1]]
        for i in range(n - 1):
            lst = tri[i]
            L = [1]
            for j in range(len(lst) - 1):
                L.append(lst[j] + lst[j+1])
            L.append(1)
            tri.append(L)
    return tri
