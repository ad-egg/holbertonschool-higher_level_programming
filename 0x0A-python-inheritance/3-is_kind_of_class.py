#!/usr/bin/python3
"""
this module contains a function that checks if an object is an instance
of a class or an instance of a class that is inherited from a specified class
"""


def is_kind_of_class(obj, a_class):
    """
    this function returns True if an object is an instance of, or if object is
    an instance of a class that inherited from the inherited class, otherwise
    it returns False
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
