a = [-5, 4, 6, -3, 4, -1]


def max_sub_array():
    curr_sum = 0
    max_sum = 0

    for i in range(len(a)):
        curr_sum = curr_sum + a[i]
        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0
    return max_sum


print(max_sub_array())


def max_sub():
    curr_sum = a[0]
    max_sum = a[0]
    for i in range(1, len(a)):
        curr_sum = max(a[i], curr_sum + a[i])
        max_sum = max(curr_sum, max_sum)

    return max_sum
