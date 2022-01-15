arr = [5, 4, 3, 2, 1]


def cycle_sort():
    i = 0
    while i <= len(arr) - 1:
        correct = arr[i] - 1
        if correct == i:
            i += 1
        else:
            arr[i], arr[correct] = arr[correct], arr[i]
    return arr


print(cycle_sort())
