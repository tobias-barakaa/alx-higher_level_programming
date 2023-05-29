#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in my_list:
            if x > my_list:
              print(i, end=" ")
              count += 1
    except:
        pass
    finally:
        print()
        return count
