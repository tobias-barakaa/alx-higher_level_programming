#!/usr/bin/env python3

import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = 'add_item.json'

# Load existing list from the file if it exists, or create an empty list
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)

