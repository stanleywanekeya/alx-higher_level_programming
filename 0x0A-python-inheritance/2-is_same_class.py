#!/usr/bin/python3
"""checks for bool instance"""


def is_same_class(obj, a_class):
    """checks if class if of instance

    Args:
        obj (any): The object to check
        a_class (type): the class to match
    Returns:
        if the object is instance of class True
        else False
    """
    def is_same_class(obj, a_class):
        if type(obj) == a_class:
            return True
        return False
