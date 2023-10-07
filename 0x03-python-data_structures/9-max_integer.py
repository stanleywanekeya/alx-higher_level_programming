#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    big = -1
    for i in range(size):
        if my_list[i] > big:
            big = my_list[i]
    return (big)
