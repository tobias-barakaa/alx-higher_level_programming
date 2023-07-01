#!/usr/bin/python3
"""function that appendds text to each line"""


def append_after(filename="", search_string="", new_string=""):
    """function that appendds text to each line"""
    app_msg = ""
    with open(filename, 'r') as f:
        elem_line = f.readline()
        while elem_line != "":
            app_msg += elem_line
            if search_string in elem_line:
                app_msg += new_string
            elem_line = f.readline()
    with open(filename, 'w') as f:
        f.write(app_msg)
