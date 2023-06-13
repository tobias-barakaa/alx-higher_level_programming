#!/usr/bin/python3

"""function to count characters"""


def write_file(filename="", text=""):
    """function to write text to a file"""
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
