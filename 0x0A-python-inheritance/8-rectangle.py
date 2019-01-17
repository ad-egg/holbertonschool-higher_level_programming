#!/usr/bin/python3
"""
this module contains a class Rectangle that inherits from class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this class inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        instantiates with width and height
        """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
