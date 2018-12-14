#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    k = sorted(a_dictionary.keys())
    for i in range(0, len(k)):
        if k[i] in a_dictionary:
            print("{}: {}".format(k[i], a_dictionary[k[i]]))
