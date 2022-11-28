# sum till n

def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

print(sum_n(2))


def pow(n, p):
    if p == 0:
        return 1
    else:
        return n*pow(n, )