#!/usr/bin/python3

def divisible_by_2(my_list=[]):
     outcome = []
     for num in my_list:
        if num % 2 == 0:
            outcome.append(True)
        else:
            outcome.append(False)
     return outcome

