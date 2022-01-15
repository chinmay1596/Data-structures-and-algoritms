num = 86


def setkbit(k):
    return (num | (1 << (k - 1))) >> (k - 1)

print(setkbit(4))