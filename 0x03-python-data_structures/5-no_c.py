#!/usr/bin/python3

def no_c(my_string):
    return "".join([ch for ch in list(my_string) if ch not in ["c", "C"]])
