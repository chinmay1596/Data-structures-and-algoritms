
def is_safe(maze, i, j, row, col, visited)->bool:
    if (i>=0 and i < row) and (j>=0 and j < col) and maze[i][j] == 1 and visited[i][j] == False:
        return True
    return False

def solve_maze(maze:list, row:int, col:int, i:int, j:int, visited:list, path:list, output:str):
    if i == row-1 and j == col-1:
        path.append(output)
        return

    # down
    if is_safe(maze, i+1, j, row, col, visited):
        visited[i+1][j] = True
        solve_maze(maze, row, col, i+1, j, visited, path, output+'D')
        visited[i+1][j] = False
    
    # right
    if is_safe(maze, i, j+1, row, col, visited):
        visited[i][j+1] = True
        solve_maze(maze, row, col, i, j+1, visited, path, output+'R')
        visited[i][j+1] = False

    # left
    if is_safe(maze, i, j-1, row, col, visited):
        visited[i][j-1] = True
        solve_maze(maze, row, col, i, j-1, visited, path, output+'L')
        visited[i][j-1] = False

    
    # up
    if is_safe(maze, i-1, j, row, col, visited):
        visited[i-1][j] = True
        solve_maze(maze, row, col, i-1, j, visited, path, output+'U')
        visited[i-1][j] = False


if __name__ == '__main__':
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    row = 4
    col = 4

    visited = [
        [True, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False]
    ]
   
    path = []
    output = ""

    solve_maze(maze, row, col, 0, 0, visited, path, output)
    print(path)