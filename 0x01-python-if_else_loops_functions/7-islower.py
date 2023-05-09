#!/usr/bin/python3
def islower(c):
    """function to check if char is lowercase"""
    if ord(c) in range(97, 123):
        return True
    else:
        return False
