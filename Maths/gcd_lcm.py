def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(14, 8))


def lcm(a, b):
    return a * b // gcd(a, b)


# print(lcm(14, 8))
