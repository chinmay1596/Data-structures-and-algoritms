num = 182


def findbit(n):
    return (num & (1 << (n - 1))) >> (n-1)


print(findbit(5))
