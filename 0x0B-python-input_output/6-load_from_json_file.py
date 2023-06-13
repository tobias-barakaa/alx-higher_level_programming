#!/usr/bin/python3
"""json file print"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON data.

    Raises:
        FileNotFoundError: If the specified file is not found.
        ValueError: If the JSON data cannot be parsed.

    """
    with open(filename, 'r') as file:
        return json.load(file)
