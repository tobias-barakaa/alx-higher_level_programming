#!/usr/bin/python3
import json

"""function to return a json representation"""


def to_json_string(my_obj):
    """return json to string object"""
    json_data = json.dumps(my_obj)
    return json_data
