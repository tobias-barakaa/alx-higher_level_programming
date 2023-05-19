#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for index, item in enumerate(my_list):
        if isinstance(item, list):
            if index == replace:
                my_list[index] = search
