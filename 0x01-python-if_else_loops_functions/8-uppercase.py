#!/usr/bin/python3
def uppercase(str):
    """function to uppercase lowercase string"""
    for i in str:
        print("{}".format((chr(ord(i) - 32)) if ord(i) in range(97, 123)
                          else i), end="")
    print()
