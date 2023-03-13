def find_last_index(arr, index, target):
    if index < 0:
        return -1
    if arr[index] == target:
        return index
    return find_last_index(arr, index - 1, target)


arr3 = [1, 3, 2, 3, 6, 4, 2, 3]
target = 3

print(find_last_index(arr3, len(arr3) - 1, target))
