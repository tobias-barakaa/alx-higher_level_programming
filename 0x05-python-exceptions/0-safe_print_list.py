#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        counting = 0
        for i in my_list:
            counting += 1
            if counting <= x:
                print(i, end=" ")
            else:
                break
        print()
        return counting
    except:
        return 0
