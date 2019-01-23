#!/usr/bin/python3
"""
this module contains a class Rectangle
"""


class Rectangle(Base):
    """
    a class Rectangle that inherits from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiates an instance of Rectangle with width, height, and id
        """
        super().__init__(id)  # call super class with id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        gets the width of an instance of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of an instance of Rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        gets the height of an instance of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of an instance of Rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
        gets x of an instance of Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the x of an instance of Rectangle
        """
        self.__x = value

    @property
    def y(self):
        """
        gets y of an instance of Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the y of an instance of Rectangle
        """
        self.__y = y
