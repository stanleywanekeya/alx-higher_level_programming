#!/usr/bin/python3
"""Returns obj as dictionary representation"""


class Student:
    """Defines student class"""

    def __init__(self, first_name, last_name, age):
        """initializes student class

        Args:
            first_name (str): name argument
            last_name (str): name argument
            age (int): integer argument
            """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs=None):
            """Returns dict representation of class

            Args:
                attr (list): list argument
            """

            if (type(attrs) == list and 
                    all(type(ele) == str for ele in attrs)):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
