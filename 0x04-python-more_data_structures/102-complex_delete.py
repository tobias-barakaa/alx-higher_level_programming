#!/usr/bin/python3 
def complex_delete(a_dictionary, value):
    for j, s in list(a_dictionary.items()):
        if s is value:
            a_dictionary.pop(j)
    return a_dictionary
