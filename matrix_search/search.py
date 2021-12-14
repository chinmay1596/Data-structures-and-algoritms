matrix = [
    [10, 20, 30, 40],
    [15, 25, 35, 45],
    [28, 29, 37, 49],
    [33, 34, 38, 50]
]
target = 37

# time complexity O(n)

def matrix_sort():
    low = 0
    high = len(matrix)-1

    while low < len(matrix) and high >= 0:
        if matrix[low][high] == target:
            return f'{[low, high]}'
        elif matrix[low][high] > target:
            high -= 1
        elif matrix[low][high] < target:
            low+=1

    return [-1, -1]

print(matrix_sort())