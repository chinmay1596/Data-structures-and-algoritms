# find element appearing once

num = [2, 3, 4, 1, 2, 1, 3, 6, 4]


def ans():
    unique = 0

    for i in num:
        unique = unique ^ i
    return unique


print(ans())
