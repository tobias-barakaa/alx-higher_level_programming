#!/usr/bin/python3

def max_integer(my_list):
    length_list = len(my_list)
    if length_list == 0:
        return None
    else:
        max_elem = my_list[0]
        for i in my_list:
            if i > max_elem:
                max_elem = i
        return max_elem
