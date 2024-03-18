#!/usr/bin/python3
# Hamud001


def print_matrix_integer(matrix=[[]]):
    """function that prints matrix of integers."""
    for n in range(len(matrix)):
        for j in range(len(matrix[n])):
                print("{:d}".format(matrix[n][j]), end="")
                if j != (len(matrix[n]) - 1):
                    print(" ", end="")

        print("")
