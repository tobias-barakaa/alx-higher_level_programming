#!/usr/bin/python3

def remove_chars(my_string) :
    return "".join(list([char for char in list(my_string) if char not in ["c", "C"]]))
