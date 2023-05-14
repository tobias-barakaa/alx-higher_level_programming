#!/usr/bin/python3

def reverse_list(my_list=[]):
    left = 0
    right = len(my_list) - 1
    while left < right:
        # Swap
        temp = my_list[left]
        my_list[left] = my_list[right]
        my_list[right] = temp
        left += 1
        right -= 1

    return my_list

my_list = [1, 2, 3, 4, 5]
print(reverse_list(my_list))
