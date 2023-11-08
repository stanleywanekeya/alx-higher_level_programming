#!/usr/bin/python
"""Writes string to tet file"""


def write_file(filename="", text=""):
    """Writes string to textfile

    Args:
        filename (str): text file
        text (str): string to be written
    Return:
        number of characters writter
        """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
