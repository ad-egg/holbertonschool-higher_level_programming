#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        strlength = 0
        firstchar = None
    else:
        strlength = len(sentence)
        firstchar = sentence[0]
    my_tuple = (strlength, firstchar)
    return my_tuple
