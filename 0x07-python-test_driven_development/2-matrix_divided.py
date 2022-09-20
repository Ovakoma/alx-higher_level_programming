#!/usr/bin/python3
'''function divides elements of a matrix'''
def matrix_divided(matrix, div):
    ''' function definition
    Args:
        matrix: must be a lists of integers or floats
        div(int/float): must be a number(integer or float)
    Return: new matrix
    '''
    new_matrix = []

    if (not isinstance(matrix, list) or matrix == [] or
    not all(isinstance(row, list) for row in matrix) or
    not all((type(elem) in [int, float]) for elem in 
    [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists) of '
                'integers/floats')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(num / div, 2) for num in row] for row in matrix]
