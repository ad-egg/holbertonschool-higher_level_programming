#!/usr/bin/python3
"""
this module contains a function that writes an object to a text file using
JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    this function
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
