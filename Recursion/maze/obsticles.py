arr = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]


def path_restrictions(p, arr, row, col):
    if row == len(arr) - 1 and col == len(arr[0]) - 1:
        print(p)
        return

    if not arr[row][col]:
        return

    if row < len(arr) - 1:
        path_restrictions(p + "D", arr, row + 1, col)

    if col < len(arr[0]) - 1:
        path_restrictions(p + "R", arr, row, col + 1)


path_restrictions("", arr, 0, 0)
