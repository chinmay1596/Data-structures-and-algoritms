arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]


def insertion_sort():
    for i in range(len(arr) - 1):
        j = i + 1
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
            j -= 1
    return arr


print(insertion_sort())
