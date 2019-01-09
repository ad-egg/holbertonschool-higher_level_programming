#!/usr/bin/python3
"""This module makes a class Square and has a private instance attribute size.
"""


class Square:
    """a square is a parallelogram
    Attributes:
    __size: instantiates Square with size
    size must be an integer that is 0 or greater
    __position: not sure what it does
    """

    def __init__(self, size=0, position=(0, 0)):
        """this function instantiates with size private instance attribute
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """this function returns the area of the square
        """

        return self.__size ** 2

    @property
    def size(self):
        """this property retrieves the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """this sets the size I guess
        """
        self.__size = value

    @property
    def position(self):
        """this property retrieves the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position
        """
        self.__position = value

    def my_print(self):
        """this function prints the square with the hash character
        """
        if self.__size == 0:
            print()
        else:
            for emptyrow in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for octothorpe in range(0, self.__size):
                    print("#", end="")
                print()
