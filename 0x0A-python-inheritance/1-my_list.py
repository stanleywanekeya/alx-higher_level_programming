#!/usr/bin/python3
"""prints baseclass list"""


class MyList(list):
    """impliments sorted printing"""

    def print_sorted(self):
        """prints list in sorted order"""
        print(sorted(self))
