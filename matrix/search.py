"""
Matrix sorted in row wise and col wise
"""

matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [28, 29, 37, 49],
    [33, 34, 38, 50]
]
target = 37


# time complexity O(n)

def matrix_sort():
    row = 0
    col = len(matrix) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return f'{[row, col]}'
        elif matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1

    return [-1, -1]


print(matrix_sort())
