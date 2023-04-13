def quicksort(arr, start, end):
    if start >= end:
        return

    p = partition(arr, start, end)

    quicksort(arr, start, p - 1)
    quicksort(arr, p + 1, end)


def partition(arr, start, end):
    pivot = arr[start]

    count = 0
    for i in range(start + 1, end + 1):
        if arr[i] <= pivot:
            count += 1

    pivot_correct_pos = start + count
    arr[start], arr[pivot_correct_pos] = arr[pivot_correct_pos], arr[start]

    i = start
    j = end

    while i < pivot_correct_pos and j > pivot_correct_pos:

        while arr[i] <= pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i < pivot_correct_pos and j > pivot_correct_pos:
            arr[i], arr[j] = arr[j], arr[i]

    return pivot_correct_pos


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)

    quicksort(arr, 0, n - 1)

    print(arr)
