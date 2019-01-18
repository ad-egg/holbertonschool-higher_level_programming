#!/usr/bin/python3
"""
this module contains a function that returns the number of lines of a text
file
"""


def number_of_lines(filename=""):
    """
    this function returns the number of lines of a text file
    """
    with open(filename) as f:
        return len(f.readlines())
