#!/usr/bin/python3
"""
this module contains a function that reads n lines of a text file and
prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    this function reads up to n lines of a text file and prints it to stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        numlines = len(f.readlines())
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= numlines:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
