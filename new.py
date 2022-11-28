# def fib(a, b, c):
#     if c == 0:
#         return a
#     if c == 1:
#         return b
#     return fib(a, b, c - 1) ^ fib(a, b, c - 2)
#
#
# t = int(input())
# for i in range(t):
#     a, b, c = map(int, input().split())
#     print(fib(a, b, c))


def string_len(s: str, index):
    count = 0
    if index == len(s):
        return count
    count += 1
    a = string_len(s, index + 1)
    count += a
    return count


# print(string_len('GEEKSFORGEEKS', 0))

def print_triangle(arr):
    if len(arr) < 1:
        return

    temp_arr = [0] * (len(arr) - 1)
    for i in range(len(arr) - 1):
        temp_arr[i] = arr[i] + arr[i + 1]

    print_triangle(temp_arr)
    print(arr)


# print_triangle([1, 2, 3, 4, 5])

def max_min(arr, index):
    max_num = 0
    min_num = 0
    if index == len(arr):
        return max_num, min_num
    max_num = arr[index]
    min_num = arr[index]
    a, b = max_min(arr, index + 1)
    if a > max_num:
        max_num = a
    if b < min_num:
        min_num = b
    return max_num, min_num


arr = [1, 4, 45, 6, 10, -8]


# print(max_min(arr, 0))


def sum_digit(num):
    s = 0
    if num <= 0:
        return s
    s += num % 10
    sum_n = sum_digit(num // 10)
    s += sum_n
    return s


# print(sum_digit(12345))


def prod_digit(x, y):
    pass



print(sum_digit(12345))
