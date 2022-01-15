num = 5


def resetkbit(k):
    return num & (~(1 << (k - 1)))


print(resetkbit(1))
