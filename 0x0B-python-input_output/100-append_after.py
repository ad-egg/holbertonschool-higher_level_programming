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
        for y in range(len(lines)):
            line = lines[y]
            if len(line) > len_targetstr:  # line may have target str
                for x in range(len(line) - len_targetstr + 1):
                    if line[x] == search_string[0]:  # matches first letter
                        for i in range(1, len_targetstr):
                            if line[x + i] != search_string[i]:  # not a match
                                break
                            if i == len_targetstr - 1 and line[
                                 x + i] == search_string[i]:  # it is a match
                                lines.insert(y + 1, new_string)  # insert here
        f.seek(0)  # move cursor back to beginning bc readlines() moved to end
        for line in lines:
            f.write(line)
