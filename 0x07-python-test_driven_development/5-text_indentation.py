#!/usr/bin/python3
# 5-text_indentation.py
"""define function to print text"""


def text_indentation(text):
    """function to print text and add 2 new lines after
    : or ? or .

    Args:
        text (str) : text to be printed must be string

    return: will print text and 2 new lines after : ? .
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0

    while i < len(text):
        if text[i] in ["?", ":", "."]:
            print(text[i])
            print()
            i += 1
            while text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
