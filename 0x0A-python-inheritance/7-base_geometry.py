#!/usr/bin/python3
"""
this module contains a class BaseGeometry
"""


class BaseGeometry:
    """
    this is a class BaseGeometry with a public instance method for the area
    """
    def area(self):
        """
        this method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this method validates value
        """
        if isinstance(value, int) is False:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
