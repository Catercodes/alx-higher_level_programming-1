#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
# squared_matrix  is an empty list to store the squared matrix
    for row in matrix:
        squared_row = []
        for element in row:
            squared_element = []
            squared_element = element ** 2
            squared_row.append(squared_element)
# elements and row are  been  stored in the squared_matrix
        squared_matrix.append(squared_row)
    return squared_matrix
