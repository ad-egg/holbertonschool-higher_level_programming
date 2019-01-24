#!/usr/bin/python3
"""
this module contains a class Base
"""


import json


class Base:
    """
    a class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        instantiates an instance of class Base
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__class__.__name__)
        json_str = Base.to_json_string(list_objs)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)
