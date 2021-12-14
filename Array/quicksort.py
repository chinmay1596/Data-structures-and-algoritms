arr = [4, 6, 2, 5, 7, 9, 1, 3]


def partition(l, h):
    pivot = arr[l]
    i = l
    j = h
    while i < j:
        while arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def quicksort(l, h):
    if l < h:
        pivot = partition(l, h)
        quicksort(l, pivot - 1)
        quicksort(pivot + 1, h)

    return arr


print(quicksort(0, len(arr) - 1))
