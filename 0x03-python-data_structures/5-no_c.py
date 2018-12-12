#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    newstring = ""
    for i in range(0, len(my_string)):
        if (my_string[i] == 'c') or (my_string[i] == 'C'):
            continue
        newstring = newstring + my_string[i]
    return newstring
