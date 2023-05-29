#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints integers from a list
    Returns the count of printed integers
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count
