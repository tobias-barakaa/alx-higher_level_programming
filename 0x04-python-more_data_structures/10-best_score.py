#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max = float('-inf')
    key_base = None
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            key_base = key

    return key_base
