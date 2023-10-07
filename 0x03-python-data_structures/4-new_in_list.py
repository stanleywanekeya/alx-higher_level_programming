#!/usr/bin/python3
from copy import copy


def new_in_list(my_list, idx, element):
    size = len(my_list)
    new_list = copy(my_list)
    if idx < 0:
        return (new_list)
    elif idx > size:
        return (new_list)
    else:
        new_list[idx] = element
        return (new_list)
