#!/usr/bin/python3
# Graham S. Paul (101-square_matrix_map.py)
def square_matrix_map(matrix=[]):
    return list(map(lambda x: (list(map(lambda y: y * y, x))), matrix))
