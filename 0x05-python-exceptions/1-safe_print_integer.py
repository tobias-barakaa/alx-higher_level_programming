#!/usr/bin/python3

"""
  function to print values
  Return True or false
"""
def safe_print_integer(value):
       try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        print("")
        return False
