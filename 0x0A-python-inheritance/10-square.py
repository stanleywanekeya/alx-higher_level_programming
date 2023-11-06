#!usr/bin/python3
"""class square inherits from square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherits from  rectangle"""

    def __init__(self, size):
        """initializes from square
        Args:
            size (int): size of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
