#!/usr/bin/python3

# Import statements should come before other code
from add_0 import add

# Use two blank lines to separate top-level functions and classes
if __name__ == "__main__":

    # Use four spaces for indentation
    # Remove unnecessary comment
    a = 1
    b = 2

    # Use string formatting to make the code more readable
    print("{} + {} = {}".format(a, b, add(a, b)))
