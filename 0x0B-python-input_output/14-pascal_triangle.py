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
            if x == 0:
                row.append(begin)
            else:
                if y > 0:
                    if x < y:
                        row.append(triangle[y - 1][x] + triangle[y - 1][x - 1])
                    else:
                        row.append(begin)
        triangle.append(row)
    return triangle
