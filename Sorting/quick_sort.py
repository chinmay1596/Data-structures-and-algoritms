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

    # count elements smaller than pivot for its right position in arr
    count = 0
    for k in range(s + 1, e + 1):
        if arr[k] <= pivot:
            count += 1
    # index of where to put our pivot on its correct position based on smaller elements count
    pivot_index = s + count

    # swap karlo
    arr[s], arr[pivot_index] = arr[pivot_index], arr[s]

    i = s
    j = e
    while i < pivot_index and j > pivot_index:

        while arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < pivot_index and j > pivot_index:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return pivot_index


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)

    quicksort(arr, 0, n - 1)

    print(arr)
