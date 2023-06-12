#!/usr/bin/python3
"""function to play with class int"""


class MyInt(int):
    """class int"""

    def __eq__(self, other):
        """invert boolen values of equal"""

        return False

    def __ne__(self, other):
        """invert boolen value of not equal"""

        return True
