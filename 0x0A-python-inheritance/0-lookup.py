#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    this function returns the list of available attributes and methods of an object.
    """
    att_meth = []
    for thing in dir(obj):
        att_meth.append(thing)
    return att_meth
