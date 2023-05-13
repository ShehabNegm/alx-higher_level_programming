#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """function to print a given matrix"""

    if matrix == [[]]:
        print("{}".format(""))

    else:
        for i in matrix:
            for j in i[:-1]:
                print("{:d}".format(j), end=" ")
            print("{:d}".format(i[-1]))
