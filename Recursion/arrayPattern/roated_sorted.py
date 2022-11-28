arr = [5, 6, 7, 8, 9, 1, 2, 3]
target = 1


def search(start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if target == arr[mid]:
        return mid

    if arr[start] <= arr[mid]:
        if target >= arr[start] and target <= arr[mid]:
            return search(start, mid - 1)
        else:
            return search(mid + 1, end)
    if target >= arr[mid] and target <= arr[end]:
        return search(mid + 1, end)
    return search(start, mid - 1)


print(search(0, len(arr) - 1))
