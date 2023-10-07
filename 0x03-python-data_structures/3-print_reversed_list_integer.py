#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    for i in range(size):
        print("{}".format(my_list[size - i - 1]))
