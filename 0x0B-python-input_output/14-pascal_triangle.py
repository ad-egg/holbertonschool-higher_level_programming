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
    begin = 1
    for y in range(0, n):
        row = []
        for x in range(0, y + 1):
            if y == 0 or x == 0 or (y > 0 and x == y):
                row.append(begin)
            else:
                row.append(triangle[y - 1][x] + triangle[y - 1][x - 1])
        triangle.append(row)
    return triangle
