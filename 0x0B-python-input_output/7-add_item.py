#!/usr/bin/env python3
"""Script that adds all arguments to a Python list and saves them to a file"""

import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, "add_item.json")
