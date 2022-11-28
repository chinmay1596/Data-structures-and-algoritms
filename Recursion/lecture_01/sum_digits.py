
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sum_digits(n//10)

# print(sum_digits(123))


def digit_product(n):
    if n%10 == n:
        return n
    else:
        return (n%10) * digit_product(n//10)


print(digit_product(123))