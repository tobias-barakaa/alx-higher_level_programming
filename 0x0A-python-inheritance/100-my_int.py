#!/usr/bin/python3

"""function that inherits from int"""


class MyInt(int):
    def __eq__(self, other):
        """
        Overrides the == operator to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert its behavior.
        """
        return super().__eq__(other)
