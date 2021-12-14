arr1 = [9, 4, 7, 6, 3, 1, 5]
# arr2 = [0, 0, 0, 0, 0, 0, 0]


def merge(l, mid, r):
    i = l
    j = mid + 1
    k = l

    while i <= mid and j <= r:
        if arr1[i] < arr1[j]:
            arr1[k] = arr1[i]
            i += 1
        else:
            arr1[k] = arr1[j]
            j += 1
        k += 1
    if i < mid:
        while i <= mid:
            arr1[k] = arr1[i]
            i += 1
            k += 1
    else:
        while j <= r:
            arr1[k] = arr1[j]
            j += 1
            k += 1


def mergesort(l, r):
    # import pdb
    # pdb.set_trace()
    if l < r:
        mid = (l + r) // 2
        mergesort(l, mid)
        mergesort(mid + 1, r)
        merge(l, mid, r)
    return arr1


print(mergesort(0, len(arr1) - 1))
