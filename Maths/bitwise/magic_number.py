def magic_number(n):

    ans = 0
    base = 1
    while n > 0:
        last = n & 1
        n = n >> 1
        base*=5
        ans += base * last
    return ans

print(magic_number(4))