#!/usr/bin/python3
def magic_string():
    count = 0
    magic_string.n = getattr(magic_string, 'n', count) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
