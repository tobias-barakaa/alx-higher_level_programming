#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0  # Variable to keep track of the number of elements printed

    try:
        for i in range(x):
            print(my_list[i], end=" ")  # Print the element without a new line
            count += 1
    except IndexError:
        pass
    finally:
        print()  # Print a new line
        return count
