#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    new_list = []
    for x in reversed(my_list):
     new_list.append(x)

    print(new_list)
