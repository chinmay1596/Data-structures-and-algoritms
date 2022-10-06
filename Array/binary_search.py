arr = [-1, 0, 3, 5, 9, 12]
key = 2


def binary_search_iterative():
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
    else:
        return 'No element found'


# print(binary_search())


def binary_search(arr, low, high):
    """
    recursive method
    :param arr:
    :param low:
    :param high:
    :return:
    """
    if low >= high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    if key > arr[mid]:
        return binary_search(arr, mid + 1, len(arr) - 1)
    if key < arr[mid]:
        return binary_search(arr, 0, mid - 1)


print(binary_search(arr, 0, len(arr) - 1))
