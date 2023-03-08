from typing import List


def setZeroes(self, matrix: List[List[int]]) -> None:
    row_zero = False
    column_zero = False

    rows = len(matrix)
    columns = len(matrix[0])

    for i in range(rows):
        if matrix[i][0] == 0:
            column_zero = True

    for j in range(columns):
        if matrix[0][j] == 0:
            row_zero = True

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0

    if row_zero:
        for j in range(columns):
            matrix[0][j] = 0

    if column_zero:
        for i in range(rows):
            matrix[i][0] = 0