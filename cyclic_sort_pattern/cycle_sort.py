arr = [5, 4, 3, 2, 1]


def cycle_sort():
    i = 0
    while i < len(arr):
        correct_index = arr[i] - 1
        if correct_index == i:
            i += 1
        else:
            arr[i], arr[correct_index] = arr[correct_index], arr[i]
    return arr


print(cycle_sort())
