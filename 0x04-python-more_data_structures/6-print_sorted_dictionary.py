#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """function to print items of sorted dict"""

    if a_dictionary:

        d = sorted(a_dictionary)

        for i in d:
            print("{}: {}".format(i, a_dictionary[i]))
