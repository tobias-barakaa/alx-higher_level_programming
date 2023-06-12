#!/usr/bin/python3

def lookup(object):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve the attributes and methods.

    Returns:
        A list containing the names of the attributes and methods available for the object.

    Examples:
    """
    return dir(object)
