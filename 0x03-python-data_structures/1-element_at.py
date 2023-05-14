#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
     return None
    else:
        print("Element at index {} is {}".format(my_list[idx], idx))
