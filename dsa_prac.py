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


def firstBadVersion(n):
    start = 0
    end = n
    
    while start <= end:
        mid = (start + end)//2
        bad = isBadVersion(mid) 
        if bad:
            return mid
        elif not bad:
            start = mid+1
        else:
            end = mid-1