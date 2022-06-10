matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = 0
col = 0
l = []
while row < len(matrix):
    s = 0
    s += matrix[row][col]
    if col < len(matrix):
        col += 1
    else:
        pass