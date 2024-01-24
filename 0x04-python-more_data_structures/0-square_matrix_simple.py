#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    output = []
    for row in matrix:
        squared_row = [element ** 2 for element in row]
        output.append(squared_row)
    return output
