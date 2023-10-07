#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        size = len(i)
        for s in range(size):
            if i[s] == 'c' or i[s] == 'C':
                i.remove(i[s])
