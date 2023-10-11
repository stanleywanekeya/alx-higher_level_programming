#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    key = list(a_dictionary.keys())
    for i in key:
        num += 1
    return num
