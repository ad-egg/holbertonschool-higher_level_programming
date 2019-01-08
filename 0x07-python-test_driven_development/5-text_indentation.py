#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after certain characters.
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each period, question
    mark, and colon.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("\n")
            while i < len(text) - 1:
                if text[i + 1] == ' ':
                    i += 1
                else:
                    break
        i += 1
