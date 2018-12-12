#!/usr/bin/python3
def multiple_returns(sentence):
    strlength = len(sentence)
    if len(sentence) == 0:
        firstchar = None
    else:
        firstchar = sentence[0]
    my_tuple = (strlength, firstchar)
    return my_tuple
