def print_arr(arr, index):
    if index == len(arr):
        return
    print(arr[index])
    print_arr(arr, index + 1)


print_arr([1, 2, 3, 4, 5, 6], 0)


def print2(arr):
    if len(arr) == 0:
        return
    print(arr[0])
    print2(arr[1:])


arr1 = [1, 2, 3, 4, 5, 6]

print2(arr1)
