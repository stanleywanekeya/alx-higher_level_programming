#!/usr/bin/python3
"""Defines class for json"""


class Student:
    """class student defined"""

    def __init__(self, first_name, last_name, age):
        """initializes class student

        Args:
            first_name (str): name argument
            last_name (str): name argument
            age (int): integer argument
            """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves info in dictionary"""
        return self.__dict__
