#!/usr/bin/python3
"""write a json data to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    """

    # Serialize the object to JSON
    json_data = json.dumps(my_obj)

    # Open the file and write the JSON data
    with open(filename, mode='w') as file:
        file.write(json_data)
