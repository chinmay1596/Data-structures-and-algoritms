def find_all_index(arr, index, target, res=[]):
    if index == len(arr):
        return res
    if arr[index] == target:
        res.append(index)
    return find_all_index(arr, index + 1, target)


arr3 = [1, 3, 2, 3, 6, 4, 2, 3]
target = 3

print(find_all_index(arr3, 0, target))



def find_all_index(arr, index, target, res):
    if index == len(arr):
        return res
    if arr[index] == target:
        res.append(index)
    return find_all_index(arr, index + 1, target, res)


arr3 = [1, 3, 2, 3, 6, 4, 2, 3]
target = 3
res = []

print(find_all_index(arr3, 0, target, res))
