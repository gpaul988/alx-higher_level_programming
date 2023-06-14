#!/usr/bin/python3
# Graham S. Paul (101-square_matrix_map.py)

def square_matrix_map(matrix=[]):
    return (list(map(lambda i: list(map(lambda x: x**2, i)), matrix)))
