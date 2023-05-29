#!/usr/bin/python3

"""
  function to print values
  Return True or false
"""
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        print("")
        return True
    except (ValueError, TypeError):
        return False

