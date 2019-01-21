#!/usr/bin/python3
"""
this module contains a function that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts new_string after a line that contains search_string
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()  # list of all lines
        len_targetstr = len(search_string)
        len_new = len(new_string)
        for y in range(len(lines)):
            if len(lines[y]) > len_targetstr:  # line may have target str
                for x in range(len(lines[y]) - len_targetstr + 1):
                    if lines[y][x] == new_string[0]:
                        for i in range(1, len_new):
                            if lines[y][x + i] != new_string[i]:
                                break
                            lines.insert(y + 1, new_string)
        f.seek(0)
        for line in lines:
            f.write(line)
