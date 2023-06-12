#!/usr/bin/python3

"""if object is class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.
    Returns True if it is, False otherwise.
    """
    return isinstance(obj, a_class)
