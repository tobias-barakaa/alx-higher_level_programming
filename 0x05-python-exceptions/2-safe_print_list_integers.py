#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints integers from a list
    Returns the count of printed integers
    """
    count = 0
    try:
        for i in range(x):
            if type((my_list[i]) == int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
            elif type(x) == int and x > count:
                raise OverflowError
            else:
                break
    except OverflowError as e:
        return e
    print("")
    return count
