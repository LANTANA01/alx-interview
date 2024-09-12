#!/usr/bin/python3
""" Given an n x n 2d matrix
rotate it 36 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Function rotate the matrix clockwise (90 degrees)
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i] = matrix[i][::-1]
