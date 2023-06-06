#!/usr/bin/python3
""" function to print for first and last name """

def say_my_name(first_name, last_name=""):
    """
    function to print a string.

    Args:
        first_name (str): first name parameter.
        last_name (str): last name parameter.

    Raises:
        TypeError: If the first_name or last_name is not a string.

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is", first_name + " " + last_name)
