#!/usr/bin/python3
"""function to inherent list class to a child class"""


class MyList(list):
    """
    class to inherent from list class
    """

    def print_sorted(self):
        """function to print a sorted list"""
        L = self.copy()
        print(sorted(L))
