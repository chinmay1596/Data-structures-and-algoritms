def sum_n(n):
    """
    Sum of natural numbers using recursion
    :param n:
    :return:
    """
    if n == 0:
        return 0
    return n + sum_n(n - 1)


print(sum_n(2))
