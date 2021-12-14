a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
target = 5


def binary_search():
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == target:
            return mid
        elif target < a[mid]:
            low = mid + 1
        elif target > a[mid]:
            high = mid - 1
    else:
        return -1


print(binary_search())
