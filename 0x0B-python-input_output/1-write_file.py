#!/usr/bin/python3

"""function to count characters"""


def write_file(filename="", text=""):
    """function to write text to a file"""
    count = 0  # Initialize count to 0
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
        count = len(text)  # Count the number of characters in the text

    return count
