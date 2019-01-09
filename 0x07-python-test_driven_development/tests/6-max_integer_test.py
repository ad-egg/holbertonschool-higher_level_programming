#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function from 6-max_integer module
    """
    def zero_list_length(self):
        """
        tests for empty list
        """
        nothing = max_integer([])
        self.assertEqual(nothing, None)
    def two_numbers(self):
        """
        tests for passing two numbers
        """
        terror = max_integer(1, 2)
        self.assertRaises(TypeError)
    def nice_int_list(self):
        """
        tests with a list of ints
        """
        biggest = max_integer([12, 60, 36])
        self.assertEqual(biggest, 60)
    def one_string(self):
        """
        passing a string to the function
        """
        highest_ascii = max_integer("asdf")
        self.assertEqual(highest_ascii, s)
    def strings_list(self):
        """
        passing a list of strings
        """
        lomgest = max_integer(["egg", "oeuf", "fromage"])
        self.assertEqual(lomgest, fromage)
    def infinities(self):
        """
        comparing infinity and negative infinity
        """
        pos_infin = float("inf")
        neg_infin = float("-inf")
        big_infinity = max_integer([pos_infin, neg_infin])
        self.assertEqual(big_infinity, pos_infin)
    def neg_infinity_to_zero(self):
        """
        comparing negative infinity to 0
        """
        neg_infin = float("-inf")
        zero = max_integer([0, neg_infin])
        self.assertEqual(zero, 0)
if __name__ == '__main__':
    unittest.main()
