class Maze:

    def count(self, row, col):
        if row == 1 or col == 1:
            return 1

        left = self.count(row - 1, col)
        right = self.count(row, col - 1)
        return left + right

    def maze_path(self):
        pass


obj = Maze()
print(obj.count(3, 3))
