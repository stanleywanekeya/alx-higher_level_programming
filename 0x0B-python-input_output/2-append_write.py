#!usr/bin/python3
"""Appends string to a textfile"""


def append_write(filename="", text=""):
    """appends string to textfile
    Args:
        filename (str): textfile
        text (str): strings written to textfile
        """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
