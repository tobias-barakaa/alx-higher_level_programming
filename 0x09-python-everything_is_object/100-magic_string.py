#!/usr/bin/python3

"""
define function magic_string
"""


def magic_string():
    """
    function that returns a string "BestSchool" n 
    times the number of the iteration
    """

    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
