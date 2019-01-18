#!/usr/bin/python3
"""
this module contains a class Student
"""


class Student:
    """
    a class Student with public instance attributes first_name, last_name,
    age, and public method that retrieves a dictionary representation of
    the instance
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiates with first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves dictionary representation of the instance
        """
        if type(attrs) is not list:
            return self.__dict__
        else:
            attrdict = {}
            for thing in attrs:
                if type(thing) is str:
                    if thing in self.__dict__.keys():
                        attrdict[thing] = self.__dict__.get(thing)
            return attrdict

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        jsonkeys = list(json.keys())
        for k in jsonkeys:
            self.__dict__[k] = json.get(k)
