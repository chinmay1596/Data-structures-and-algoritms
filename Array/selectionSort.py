arr = [4, 1, 9, 2, 3, 6]


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_element = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_element]:
                min_element = j
        arr[i], arr[min_element] = arr[min_element], arr[i]
    return arr


print(selection_sort(arr))
