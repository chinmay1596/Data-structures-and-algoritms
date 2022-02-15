mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]


class Solution:
    new_mat = [[0] * len(mat) for _ in range(len(mat[0]))]
    def rotate(self):
        row = 0
        col = 0

        while row < len(mat):
            Solution.new_mat[col][row] = mat[row][col]
            col += 1

            if col == len(mat[0]):
                row += 1
                col = 0

        start = 0
        end = len(Solution.new_mat) - 1
        while start <= end:
            for i in range(len(Solution.new_mat)):
                Solution.new_mat[i][start], Solution.new_mat[i][end] = Solution.new_mat[i][end], Solution.new_mat[i][start]
            start += 1
            end -= 1
        return Solution.new_mat

    def check(self, new_mat, target):
        for i in range(len(new_mat)):
            for j in range(len(target)):
                if new_mat[i][j] != target[i][j]:
                    return False
        else:
            return True

    def rotation(self):
        for i in range(4):
            new_mat = self.rotate()
            if self.check(new_mat, target):
                return True
        else:
            return False


a = Solution()
print(a.rotation())
