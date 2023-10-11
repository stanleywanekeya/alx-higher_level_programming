#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixa = matrix.copy()
    for i in range(len(matrix)):
        matrixa[i] = list(map(lambda x: x**2, matrixa[i]))
    return matrixa
