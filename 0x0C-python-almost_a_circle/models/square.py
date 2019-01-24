#!/usr/bin/python3
"""
this module contains a class Square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a class Square that inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiates an instance of Square
        """
        height = size
        width = size
        super().__init__(width, height, x, y, id)
        self.__size = self.width

    def __str__(self):
        """
        returns a description of an instance of Square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                 self.id, self.x, self.y, self.__size)

    @property
    def size(self):
        """
        gets the size of an instance of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of an instance of Square
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value
            self.__size = value
