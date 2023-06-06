#!/usr/bin/python3
"""define function magc_string"""


def magic_string():
    """
    functioin that returns a string “BestSchool” n 
    times the number of the iteration
    """
    if not hasattr(magic_string, 'count'):
        magic_string.count = 0
    magic_string.count += 1
    return "BestSchool" + (", BestSchool" * (magic_string.count - 1))
