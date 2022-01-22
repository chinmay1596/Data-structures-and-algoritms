def sorted(arr, index):
    if index == len(arr) - 1:
        return True
    return arr[index] < arr[index + 1] and sorted(arr, index + 1)


arr = [1, 2, 3, 4, 5, 6, 3]
print(sorted(arr, 0))
