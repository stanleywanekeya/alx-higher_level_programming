#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    attr = size, sentence[0]
    if size == 0:
        return size, None
    else:
        return attr
