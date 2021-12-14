def n_to_1(n):
    if n == 1:
        print(n)
        return
    else:
        print(n)
        n_to_1(n - 1)





def _1_to_n(n):
    if n == 1:
        print(n)
        return
    else:
        _1_to_n(n-1)
        print(n)

_1_to_n(5)


def funboth(n):
    if n == 1:
        print(n)
        return
    else:
        print(n)
        _1_to_n(n - 1)
        print(n)