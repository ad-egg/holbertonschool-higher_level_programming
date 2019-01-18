#!/usr/bin/python3
"""
this module contains a function that returns the number of lines of a text
file
"""


def number_of_lines(filename=""):
    """
    this function returns the number of lines of a text file
    """
    numberlines = 0
    with open(filename) as f:
        for line in f:
            numberlines += 1
    return numberlines
