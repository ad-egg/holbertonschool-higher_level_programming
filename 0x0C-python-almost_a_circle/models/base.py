#!/usr/bin/python3
"""
this module contains a class Base
"""


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
