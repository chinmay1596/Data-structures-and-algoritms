def factors(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res


print(factors(20))


# O(sqrt(n))
def factors2(n):
    res = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            if n // i == i:
                res.append(i)
            else:
                res.append(i)
                res.append(n // i)
        i += 1
    return res


print(factors2(20))
