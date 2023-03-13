def find_first_index(arr, index, target):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return find_first_index(arr, index + 1, target)


arr3 = [1, 3, 2, 3, 6, 4, 3]
target = 2

print(find_first_index(arr3, 0, target))
