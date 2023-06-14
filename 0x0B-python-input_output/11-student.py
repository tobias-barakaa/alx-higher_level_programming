#!/usr/bin/python3

class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list of str, optional): List of attribute names.
                If provided, only attributes contained in this list will be retrieved.
                Otherwise, all attributes will be retrieved.

        Returns:
            dict: A dictionary representation of the Student instance.

        """
        if isinstance(attrs, list) and all(isinstance(elem, str) for elem in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Reloads attributes of the Student instance from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute-value pairs.

        """
        for key, value in json.items():
            setattr(self, key, value)
