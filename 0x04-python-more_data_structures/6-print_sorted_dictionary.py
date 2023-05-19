#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    for y in keys:
        value = a_dictionary[y]
        if isinstance(value, dict):
            print(y + ":")
            print_sorted_dictionary(value)
        else:
            print(y + ": " + str(value))
