#!/usr/bin/python3

def no_c(my_string):
    return "".join([char for char in list(my_string) if char not in ["c", "C"]])
