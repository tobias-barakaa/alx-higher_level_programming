#!/usr/bin/python3

def element_at(my_list, idx):
    if my_list(idx) < 0:
        return None
    elif my_list(idx) > 0:
        return None
    else:
        print("The element at index {} is {}.".format(idx, my_list[idx]))
