#!/usr/bin/python3
"""
this module contains a function that creates an object from a JSON file
"""


def load_from_json_file(filename):
    """
    this function creates an object from a JSON file
    """
    import json
    with open(filename) as f:
        return json.load(f)
