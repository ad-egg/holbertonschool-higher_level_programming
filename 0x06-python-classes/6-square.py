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
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
        if len(position) != 2:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        elif not isinstance(position[0], int):
            print("position must be a tuple of 2 positive integers", end = "")
            raise TypeError
        elif not isinstance(position[1], int):
            print("position must be a tuple of 2 positive integers", end = "")
            raise TypeError
        elif position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers", end = "")
            raise TypeError
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
        if not isinstance(value, int):
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
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
        if position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = value

    def my_print(self):
        """this function prints the square with the hash character
        """
        if self.__size == 0:
            print()
        else:
            for row in range(0, self.__size):
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                for hash in range(0, self.__size):
                    print("#", end="")
                print()
