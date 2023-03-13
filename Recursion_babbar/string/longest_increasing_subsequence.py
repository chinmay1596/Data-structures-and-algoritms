def solve(arr, curr, prev):
    if curr == len(arr):
        return 0

    # include
    pick = 0
    if prev == -1 or arr[curr] > arr[prev]:
        pick = 1 + solve(arr, curr + 1, curr)

    not_pick = 0 + solve(arr, curr + 1, prev)

    return max(pick, not_pick)


arr = [0, 1, 0, 3, 2, 3]
curr = 0
prev = -1

print(solve(arr, curr, prev))
