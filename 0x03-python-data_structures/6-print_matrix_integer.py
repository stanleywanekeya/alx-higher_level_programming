#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
    print()
