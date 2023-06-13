#!/usr/bin/python3
"""function to return a json representation"""
import json


def to_json_string(my_obj):
    """return json to string object"""
    json_data = json.dumps(my_obj)
    return json_data
