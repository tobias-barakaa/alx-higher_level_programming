#!/usr/bin/python3

"""function that adds 2 integers"""

def add_integer(a, b=98):
    """two intergers sum.

    Args:
       a(int or float): first parametre to add.
       b(int or float): second parameter to functioin.

    Raises:
         TypeError: if the provided is not int or float
    
    Returns:
         Addition of a and b.
    """
    if type(a) not in [int, float]:
       raise TypeError("a must be an integer")

    elif type(b) not in [int, float]:
       raise TypeError("b must be an integer")
    else:
       return int(a) + int(b)
