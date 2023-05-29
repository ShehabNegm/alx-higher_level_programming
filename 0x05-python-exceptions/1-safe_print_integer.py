#!/usr/bin/python3
def safe_print_integer(value):
    """function to print an integer safely"""

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
