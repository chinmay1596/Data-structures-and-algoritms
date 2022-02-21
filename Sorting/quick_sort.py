def quicksort(arr, s, e):
    if s >= e:
        return
    # partition karenge
    p = partition(arr, s, e)

    quicksort(arr, s, p - 1)
    quicksort(arr, p + 1, e)


def partition(arr, s, e):
    # choose pivot

    pivot = arr[s]

    # count less elements than pivot for its right position in arr
    count = 0
    for k in range(s + 1, e+1):
        if arr[k] <= pivot:
            count += 1

    pivotindex = s + count

    # swap karlo
    arr[s], arr[pivotindex] = arr[pivotindex], arr[s]

    i = s
    j = e
    while i < pivotindex and j > pivotindex:

        while arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < pivotindex and j > pivotindex:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return pivotindex


if __name__ == "__main__":
    arr = [9, 9, 9]
    n = len(arr)

    quicksort(arr, 0, n - 1)

    print(arr)
