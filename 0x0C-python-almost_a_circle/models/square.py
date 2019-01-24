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

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                if key is "id":
                    self.id = value
                elif key is "size":
                    self.size = value
                elif key is "x":
                    self.x = value
                elif key is "y":
                    self.y = value
