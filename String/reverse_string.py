a = 'vinay'


def reverse_1(a: str):
    res = ''
    for i in range(len(a) - 1, -1, -1):
        res += a[i]

    return res


print(reverse_1(a))


