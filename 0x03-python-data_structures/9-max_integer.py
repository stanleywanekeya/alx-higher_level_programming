#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return (None)
    big = -1
    for i in range(size):
        if my_list[i] > big:
            big = my_list[i]
    return (big)
