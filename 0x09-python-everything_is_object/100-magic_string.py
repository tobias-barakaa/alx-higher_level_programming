#!/usr/bin/python3
"""define function magc_string"""


def magic_string():
    """
    functioin that returns a string “BestSchool” n 
    times the number of the iteration
    """
    count = 0
    magic_string.n = getattr(magic_string, 'n', count)
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
