#!/usr/bin/python3
"""
this module contains a function that returns the JSON representation of
a string object
"""


def to_json_string(my_obj):
    """
    this function returns the JSON representation of a string object
    """
    import json
    return json.dumps(my_obj)
