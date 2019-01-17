#!/usr/bin/python3
"""
this module contains a class MyList
"""


class MyList(list):
    """
    this is a class MyList which inherits from list
    """
    def print_sorted(self):
        """
        this public instance method prints the list but sorted
        """
        sortedlist = sorted(self)
        print("[", end="")
        for index in range(len(sortedlist)):
            print("{:d}".format(sortedlist[index]), end="")
            if index < len(sortedlist) - 1:
                print(", ", end="")
        print("]")
