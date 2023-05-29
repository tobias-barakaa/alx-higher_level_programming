#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for j in range(x):
             print("{}".my_list[j], end=" ")
              count += 1
    except indexError:
        break
    finally:
        print("")
        return (count)
