#!/usr/bin/python3
# Hamud001


def square_matrix_simple(matrix=[]):
    """a function that computes the square value of all integers of a matrix."""
    new_matrix = [[number**2 for number in row] for row in matrix]
    return new_matrix
