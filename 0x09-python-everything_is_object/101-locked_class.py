#!/usr/bin/python3

"""function to define a locked function."""


class LockedClass:
    """
    function that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    """

    __slots__ = ['first_name']
