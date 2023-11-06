#!/usr/bin/python3
"""Checks for instanciation"""


def is_kind_of_class(obj, a_class):
    """checks if obj is instance of class

    Args:
        obj (any): instance of a class
        a_class (type): the class
    Return:
        truen if the instance is related to the class
        fasle if not
    """

    if isinstance(obj, a_class):
        return True
    return False
