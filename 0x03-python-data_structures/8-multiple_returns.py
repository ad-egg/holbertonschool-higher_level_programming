#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        strlength = 0
        sentence = None
    else:
        strlength = len(sentence)
    my_tuple = (strlength, sentence[0])
    return my_tuple
