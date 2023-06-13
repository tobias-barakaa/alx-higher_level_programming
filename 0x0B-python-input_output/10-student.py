#!/usr/bin/python3
"""function that that defines a student by: (based on 9-student.py)"""


class Student:
    """function that that defines a student by: (based on 9-student.py)"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return class_to_json(self)
        else:
            description = {}
            for attr in attrs:
                if hasattr(self, attr):
                    value = getattr(self, attr)
                    if isinstance(value, (list, dict, str, int, bool)):
                        description[attr] = value
            return description
