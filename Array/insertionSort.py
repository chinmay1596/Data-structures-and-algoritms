arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]


def insertion_sort():
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        else:
            arr[j+1] = temp
    return arr


print(insertion_sort())
