#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after certain characters.
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each period, question
    mark, and colon.
    """
    stringlist = []
    mystring = ""
    for car in text:
        mystring = "".join(car)
        if car == '.' or car == '?' or car == ':':
            stringlist.append(mystring)
            mystring = ""
    for lines in stringlist:
        i = 0
        while lines[i] == ' ':
            i += 1
        while i < len(lines):
            print(lines[i], end="")
            i += 1
        print("\n")
