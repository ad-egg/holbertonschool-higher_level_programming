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
        json_str = [d for d in list_dictionaries]
        return json.dumps(json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_str = Base.to_json_string(dict_list)
        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(json_str)
