#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    list_key = list(new_list.keys())
    for i in list_key:
        new_list[i] *= 2
    return new_list
