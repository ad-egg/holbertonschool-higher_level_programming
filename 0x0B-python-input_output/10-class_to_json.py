#!/usr/bin/python3
"""
this module contains a function that returns the dictionary description
with simple data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure for
    JSON serialization of an object
    """
    return obj.__dict__
