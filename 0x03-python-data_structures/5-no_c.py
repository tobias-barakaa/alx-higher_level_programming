#!/usr/bin/python3

def def no_c(my_string) :
    new_str=""

    for char in list(my_string) :
        if char not in ["c", "C"]:
            new_str += char

    return new_str
