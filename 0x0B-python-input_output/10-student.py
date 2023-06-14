#!/usr/bin/python3
"""Student class defines a student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of str): List of attribute names. If provided,
                only attributes contained in this list will be retrieved.
                Otherwise, all attributes will be retrieved.

        Returns:
            dict: Dictionary representation of the Student instance.

        """
        if isinstance(attrs, list) and \
                all(isinstance(elem, str) for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
