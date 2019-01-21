#!/usr/bin/python3
"""
this module contains a function that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts new_string after a line that contains search_string
    """
    with open(filename, 'r') as f:
        lines = f.readlines()  # list of all lines
        len_targetstr = len(search_string)
        for y in range(len(lines)):
            line = lines[y]
            if search_string in line:
                if y < len(lines) - 1:
                    lines[y + 1] = new_string + lines[y + 1]
                else:
                    lines.append(new_string)
    with open(filename, 'w') as egg:
        for line in lines:
            egg.write(line)
