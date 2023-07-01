#!/usr/bin/python3
"""addding loading and saving"""


from sys import argv
from os.path import exists

tofile_json = __import__("5-save_to_json_file").tofile_json
jso_loading = __import__("6-load_from_json_file").jso_loading

namefile = "add_item.json"
argc = len(argv)

new_list = []

if exists(namefile):
    new_list = jso_loading(namefile)

if (argc == 1):
    tofile_json([], namefile)
else:
    for i in range(1, argc):
        new_list.append(argv[i])
    tofile_json(new_list, namefile)
