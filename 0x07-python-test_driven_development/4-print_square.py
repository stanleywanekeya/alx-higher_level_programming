#!/usr/bin/python3
"""prints square with pound character"""


def print_square(size):
    """Prints square with #

        Args:
            size (int): size of the square

        Raises:
            TypeError: Raises if arg is not int
            ValueError: is size < 0

        """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
