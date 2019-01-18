#!/usr/bin/python3
"""
this module contains a function that returns a list of lists of integers
that represents Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing Pascal's triangle of n
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
