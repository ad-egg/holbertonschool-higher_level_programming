#!/usr/bin/python3
"""
this module contains a function that checks if an object is an instance
of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """
    this function returns True if the object is an instance of a class that
    inherited from the specified class, otherwise it returns False
    """
    if isinstance(obj, a_class) is True and type(obj) is not a_class:
        return True
    else:
        return False
