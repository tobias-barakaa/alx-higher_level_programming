#!/usr/bin/python3

"""
inheritance function
"""


class MyList(list):
        """
        Prints the list in sorted (ascending) order.
        """
        def print_sorted(self):
        print(sorted(self))
