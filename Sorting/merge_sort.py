def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_array = arr[0:mid]
    right_array = arr[mid:]
    left = mergesort(left_array)
    right = mergesort(right_array)

    return merge(left, right)


def merge(first, second):
    new_array = [0] * (len(first) + len(second))
    i = 0
    j = 0
    k = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            new_array[k] = first[i]
            i += 1
        else:
            new_array[k] = second[j]
            j += 1
        k += 1

    while i < len(first):
        new_array[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        new_array[k] = second[j]
        j += 1
        k += 1
    return new_array


if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    print(mergesort(arr))
