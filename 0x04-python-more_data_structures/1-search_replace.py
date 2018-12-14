#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list[:]
    for item in newlist:
        if item == search:
            newlist[newlist.index(item)] = replace
    return newlist
