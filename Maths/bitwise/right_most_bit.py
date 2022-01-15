import math

num = 182


def right_most_bit():
    return round(math.log2(num & -num) + 1)


print(right_most_bit())
