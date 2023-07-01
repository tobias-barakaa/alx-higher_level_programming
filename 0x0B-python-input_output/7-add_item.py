#!/usr/bin/python3
"""addding loading and saving"""


from sys import argv
from os.path import exists

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

namefile = "add_item.json"
argc = len(argv)

new_list = []

if exists(namefile):
    new_list = load_from_json_file(namefile)

if (argc == 1):
    save_to_json_file([], namefile)
else:
    for i in range(1, argc):
        new_list.append(argv[i])
    save_to_json_file(new_list, namefile)
