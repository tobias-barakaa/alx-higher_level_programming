#!/usr/bin/python3
"""int bool string list dict"""


def class_to_json(obj):
    """Converts an object to a dictionary description for JSON serialization"""
    description = {}
    for attr in obj.__dict__:
        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            description[attr] = value
    return description
