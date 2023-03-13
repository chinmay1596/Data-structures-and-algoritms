"""
given an array print the all elements till the one element remaining in array
"""


def solve(arr):
    if len(arr) < 1:
        return

    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
    size = len(arr) // 2
    arr = arr[:size]
    solve(arr)


arr = [1, 2, 3, 4, 5, 6, 7]


# solve(arr)


def solve_two(arr, s, e):
    if s == e:
        print(arr[e])
        return

    for i in range(s, e + 1):
        print(arr[i], end=' ')
    print()

    mid = (s + e) // 2
    solve_two(arr, s, mid)


solve_two(arr, 0, len(arr) - 1)
