def add_two_string(a, b, i, j, carry, ans):
    if i < 0 and j < 0 and carry == 0:
        return ans

    first = 0
    second = 0
    if i >= 0:
        first = int(a[i])
    if j >= 0:
        second = int(b[j])

    sum_n = first + second + carry
    last_digit = sum_n % 10
    carry = sum_n // 10
    ans += str(last_digit)

    return add_two_string(a, b, i - 1, j - 1, carry, ans)


a = '20'
b = '20'
ans = ''
res = add_two_string(a, b, len(a) - 1, len(b) - 1, 0, ans)
print(res[::-1])
