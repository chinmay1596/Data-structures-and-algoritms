def print_reverse_arr(arr, index):
    if index == len(arr):
        return
    # print(arr[index])
    print_reverse_arr(arr, index + 1)
    print(arr[index])


arr = [1, 2, 3, 4, 5, 6]

print_reverse_arr(arr, 0)
