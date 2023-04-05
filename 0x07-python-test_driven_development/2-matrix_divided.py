#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists of integers/floats): The matrix to be divided.
        div (int): The number to divide each element of the matrix by.

    Returns:
        A new matrix (list of lists of floats):
        The result of dividing each element of the input matrix by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
        or if the div is not a number.
        TypeError: If any element of the matrix is not an integer or float.
        TypeError: If any row of the matrix has a different size.
        ZeroDivisionError: If the div is equal to zero.
    """

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError
        ("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [
            [round(element / div, 2) for element in row] for row in matrix]
    return new_matrix
