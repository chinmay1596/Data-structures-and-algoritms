# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
#
# mid_matrix = len(matrix) // 2
#
# mid = len(matrix[mid_matrix]) // 2
#
# row = 0
# col = 0
# l = []
# while col >= 0 or row < len(matrix):
#     if row < len(matrix) and col < len(matrix[row]) - 1:
#         l.append(matrix[row][col])
#         col += 1
#
#     elif row < len(matrix) - 1 and col == len(matrix[row]) - 1:
#         l.append(matrix[row][col])
#         row += 1
#
#     elif row == len(matrix) - 1 and col > 0:
#         l.append(matrix[row][col])
#         col -= 1
#
#     elif row == len(matrix) - 1 and col == 0:
#         l.append(matrix[row][col])
#         row -= 1
#     else:
#         if matrix[row][col] == matrix[mid_matrix][mid]:
#             break
#         else:
#             l.append(matrix[row][col])
#             col += 1
# print(l)


n = 3
a = [11, 12, 13, 14, 15]


def xor():
    l = []
    for i in a:
        s = 0
        for j in a:
            element = i
            s += element ^ j
        l.append(s)
    print(max(l))


xor()
