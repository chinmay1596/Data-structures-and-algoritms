def max_arr(arr, index):
    if index == len(arr):
        return -1
    ans = arr[index]
    rec = max_arr(arr, index + 1)
    return max(ans, rec)


arr1 = [1, 2, 3, 4, 5]
# print(max_arr(arr1, 0))


def max_arr1(arr, index, maxi):
    if index == len(arr):
        return maxi
    maxi = max(maxi, arr[index])
    return max_arr1(arr, index + 1, maxi)


maxi = -1
arr = [1, 2, 3, 4, 5]
maxi = max_arr1(arr, 0, maxi)
print(maxi)
