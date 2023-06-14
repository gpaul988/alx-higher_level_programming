#!/usr/bin/python3
# Graham S. Paul (0-square_matrix_simple.py)
def square_matrix_simple(matrix=[]):
    return [[x * x for x in subset] for subset in matrix]
