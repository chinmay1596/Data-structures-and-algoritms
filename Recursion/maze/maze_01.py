class Maze:

    def count(self, row, col):
        if row == 0 or col == 0:
            return 1

        left = self.count(row - 1, col)
        right = self.count(row, col - 1)
        return left + right

    def path(self, p, row, col):
        if row == 0 and col == 0:
            print(p)
            return
        if row > 0:
            self.path(p+'D', row-1, col)

        if col > 0:
            self.path(p+'R', row, col-1)

    def path_ret(self, p, row, col):
        if row == 0 and col == 0:
            l = []
            l.append(p)
            return l

        ans = []
        if row > 0:
            ans.extend(self.path_ret(p+'D', row-1, col))

        if col > 0:
            ans.extend(self.path_ret(p+'R', row, col-1))
        return ans

    def path_diag(self, p, row, col):
        if row == 0 and col == 0:
            l = []
            l.append(p)
            return l

        ans = []

        if row > 0 and col > 0:
            ans.extend(self.path_diag(p + 'D', row - 1, col-1))

        if row > 0:
            ans.extend(self.path_diag(p+'V', row-1, col))

        if col > 0:
            ans.extend(self.path_diag(p+'H', row, col-1))
        return ans

obj = Maze()
# print(obj.count(2, 2))
# obj.path("", 2, 2)
# print(obj.path_ret("", 2, 2))
print(obj.path_diag("", 2, 2))