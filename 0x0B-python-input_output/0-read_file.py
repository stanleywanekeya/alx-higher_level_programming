#!/usr/bin/python3
"""Reads files"""


def read_file(filename=""):
    """reads files from filename"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
