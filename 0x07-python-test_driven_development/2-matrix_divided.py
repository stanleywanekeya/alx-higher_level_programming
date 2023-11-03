#!/usr/bin/python3
"""Function to divide matrix"""


def matrix_divided(matrix, div):
    """Function to divide matrix

        Args:
            matrix (int): contains integers
            div (int): integer argument
        """
    for i in matrix:
        if not isinstance(i, int) and not isinstance(i, float):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError("div must be a number")
        if div = 0:
            raise ZeroDivisionError

    mat = 
