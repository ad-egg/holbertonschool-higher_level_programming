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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        prints the rectangle description
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        returns the area of a rectangle
        """
        return self.__width * self.__height
