#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        if x > 0:
            for j in my_list:
                x += 1
                print("%d\n" % x)
    except:
        return None
