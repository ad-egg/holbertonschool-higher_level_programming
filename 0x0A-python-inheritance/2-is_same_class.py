#!/usr/bin/python3
"""
this module contains a function that checks if an object is an instance
of a specified class
"""


def is_same_class(obj, a_class):
    """
    this function returns True if the object is exactly an instance of the
    specified class, otherwise it returns False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
