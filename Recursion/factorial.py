"""
factorial of an number by recursion
"""


def factorial(n):
    if n == 0:
        return 1
    small = factorial(n - 1)
    ans = n * small
    return ans


print(factorial(5))
