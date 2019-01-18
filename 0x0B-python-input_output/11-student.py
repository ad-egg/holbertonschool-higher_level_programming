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

    def to_json(self):
        """
        retrieves dictionary representation of the instance
        """
        return self.__dict__
