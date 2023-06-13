#!/usr/bin/python3

"""function to count characters"""


def append_write(filename="", text=""):
    """function to write text to a file"""
    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
