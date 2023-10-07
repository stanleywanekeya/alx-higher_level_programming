#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx >= 0 and idx < size:
        return (my_list[idx])
    return (None)
