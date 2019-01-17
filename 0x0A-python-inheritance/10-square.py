#!/usr/bin/python3
"""
this module contains class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square inherits from class Rectangle
    """
    def __init__(self, size):
        """
        instantiates a Square with size
        """
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """
        returns area of a Square
        """
        return self.__size * self.__size
