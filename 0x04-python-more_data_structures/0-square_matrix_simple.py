#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    tmp = []
    for m in matrix:
        tmp.append(list(map(lambda m: m**2, m)))
    return (tmp)
