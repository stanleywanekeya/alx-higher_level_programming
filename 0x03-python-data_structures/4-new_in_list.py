#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if idx >= 0 and idx < size:
        copy = [x for x in my_list]
        copy[idx] = element
        return (copy)
    else:
        return (my_list)
