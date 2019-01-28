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
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        dict_list = []
        filename = "{}.json".format(cls.__name__)
        for obj in list_objs:
            dict_list.append(obj.to_dictionary())
        json_str = Base.to_json_string(dict_list)
        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        str_of_things = json.loads(json_string)
        return [dictionary for dictionary in str_of_things]

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        dummy = cls(6, 6, 6)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = "{}.json".format(cls.__name__)
        list_instances = []
        with open(filename) as f:
            list_dict = Base.from_json_string(f.read())
        for shape in list_dict:
            dummy = cls.create(**shape)
            list_instances.append(dummy)
        return list_instances
