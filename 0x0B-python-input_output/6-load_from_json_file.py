#!/usr/bin/env python3

import json

def create_object_from_json(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object created from the JSON data.

    Raises:
        FileNotFoundError: If the specified file is not found.
        JSONDecodeError: If the JSON data cannot be parsed.

    """
    with open(filename, 'r') as file:
        json_data = file.read()

    obj = json.loads(json_data)
    return obj
