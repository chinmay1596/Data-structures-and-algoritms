arr = [
    [True, True, True],
    [True, True, True],
    [True, True, True]
]

path = [[0] * len(arr[0]) for _ in range(len(arr))]


def all_paths(p, arr, row, col):
    if row == len(arr) - 1 and col == len(arr[0]) - 1:
        print(p)
        return

    if not arr[row][col]:
        return

    # I am considering this path
    arr[row][col] = False

    if row < len(arr) - 1:
        all_paths(p + "D", arr, row + 1, col)

    if col < len(arr[0]) - 1:
        all_paths(p + "R", arr, row, col + 1)

    if row > 0:
        all_paths(p + "U", arr, row - 1, col)

    if col > 0:
        all_paths(p + "L", arr, row, col - 1)

    arr[row][col] = True


# all_paths("", arr, 0, 0)


def all_path_print(p, arr, row, col, path, step):
    if row == len(arr) - 1 and col == len(arr[0]) - 1:
        path[row][col] = step
        for i in path:
            print(str(i))
        print(p)
        print("")
        return

    if not arr[row][col]:
        return

    # I am considering this path
    arr[row][col] = False
    path[row][col] = step
    if row < len(arr) - 1:
        all_path_print(p + "D", arr, row + 1, col, path, step + 1)

    if col < len(arr[0]) - 1:
        all_path_print(p + "R", arr, row, col + 1, path, step + 1)

    if row > 0:
        all_path_print(p + "U", arr, row - 1, col, path, step + 1)

    if col > 0:
        all_path_print(p + "L", arr, row, col - 1, path, step + 1)

    arr[row][col] = True
    path[row][col] = 0


all_path_print("", arr, 0, 0, path, 1)
