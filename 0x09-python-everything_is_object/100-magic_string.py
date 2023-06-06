#!/usr/bin/python3

def magic_string():
    """
    Returns a string "BestSchool" repeated n times, where n is the number of times the function has been called.
    """

    # Retrieve the current value of the counter attribute 'n' from the function object 'magic_string'
    # If the attribute doesn't exist, initialize it with a value of 0
    magic_string.n = getattr(magic_string, 'n', 0) + 1

    # Return a string consisting of "BestSchool" repeated n-1 times, followed by "BestSchool"
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
