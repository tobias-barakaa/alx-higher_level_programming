#!/usr/bin/python3
"""write a json data to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    """

    with open(filename, mode='w', encoding="UTF-8") as file:
        json.dump(my_obj, file)
