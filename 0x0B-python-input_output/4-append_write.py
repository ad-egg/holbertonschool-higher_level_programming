#!/usr/bin/python3
"""
this module contains a function that appends text to a file
"""


def append_write(filename="", text=""):
    """
    this function appends text to a file and returns the number of characters
    created
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
