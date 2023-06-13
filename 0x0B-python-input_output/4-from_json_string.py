#!/usr/bin/python3
"""json data to string"""
import json


def from_json_string(my_str):
    """function to return string to json"""
    data_json = json.loads(my_str)
    return data_json
