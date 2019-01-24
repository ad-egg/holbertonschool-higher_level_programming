#!/usr/bin/python3
"""
this module contains a class Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """
    a class Rectangle that inherits from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiates an instance of Rectangle with width, height, and id
        """
        super().__init__(id)  # call super class with id
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        else:
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be > 0")
        else:
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        """
        returns the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints an instance of Rectangle using '#' character
        """
        for down in range(self.__y):
            print()
        for lines in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        returns a string that describes the instance of Rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
              self.id, self.__x, self.__y, self.__width,
              self.__height)

    def update(self, *args):
        """
        assigns an argument to each attribute
        """
        if len(args) > 1:
            self.id = args[0]
        if len(args) > 2:
            self.width = args[1]
        if len(args) > 3:
            self.height = args[2]
        if len(args) > 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
