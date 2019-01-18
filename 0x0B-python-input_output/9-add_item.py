#!/usr/bin/python3
"""
this module contains a script that adds all arguents to a Python list and
saves them to a file
"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

pylist = []
arguments = argv[1:]
for string in arguments:
    pylist.append(string)
save_to_json_file(pylist, "add_item.json")
