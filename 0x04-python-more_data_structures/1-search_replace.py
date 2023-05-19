#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for index, item in enumerate(my_list):
        if isinstance(item, list):
            search_replace(item, search, replace)
        else:
            if item == search:
                my_list[index] = replace
