#!/usr/bin/python3

def search_replace(my_list, search, replace):
    extra = []
    for item in my_list:
        if item == search:
            extra.append(replace)
        else:
            extra.append(item)
    return extra
