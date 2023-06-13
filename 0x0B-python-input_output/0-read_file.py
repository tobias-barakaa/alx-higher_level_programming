#!/usr/bin/python3

"""function to read from file"""


def read_file(filename=""):
    """read file and print in stdout"""
    with open(filename, "r", encoding="utf8") as text_file:
        print(text_file.read(), end="")
