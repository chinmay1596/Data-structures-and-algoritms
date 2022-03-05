matrix = [[0, 1, 2, 3], [3, 4, 5, 2], [1, 3, 1, 5]]


class Solution:
    def setZeroes(self, matrix):
        if len(matrix) == len(matrix[0]):
            matrix1 = [[1] * len(matrix) for _ in range(len(matrix[0]))]
        else:
            matrix1 = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        row = 0
        col = 0

        while row <= len(matrix) - 1:
            if col <= len(matrix[0]) - 1 and not matrix[row][col] == 0:
                col += 1
            elif col <= len(matrix[0]) - 1 and matrix[row][col] == 0:
                self.set_matrix_zero(row, col, matrix, matrix1)
                col += 1
            else:
                row += 1
                col = 0
        self.copy_matrix(matrix, matrix1)
        matrix[:] = matrix1
        return matrix

    def set_matrix_zero(self, row, col, matrix, matrix1):
        row1 = row
        col1 = 0
        row2 = 0
        col2 = col

        matrix1[row][col] = 0

        while row2 <= len(matrix) - 1 or col1 <= len(matrix[0]) - 1:
            if col1 <= len(matrix[0]) - 1 and not matrix[row1][col1] == 0:
                matrix1[row1][col1] = 0
                col1 += 1
            else:
                if col1 <= len(matrix[0]) - 1:
                    col1 += 1

            if row2 <= len(matrix) - 1 and not matrix[row2][col2] == 0:
                matrix1[row2][col2] = 0
                row2 += 1
            else:
                row2 += 1

    def copy_matrix(self, matrix, matrix1):
        row = 0
        col = 0

        while row <= len(matrix1) - 1:
            if col <= len(matrix[0]) - 1:
                if matrix1[row][col] == 1:
                    matrix1[row][col] = matrix[row][col]
                col += 1
            else:
                row += 1
                col = 0


obj = Solution()
print(obj.setZeroes(matrix))
