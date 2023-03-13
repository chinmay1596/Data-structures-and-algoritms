def recursive_multiply(x, y):
    """
    Product of two numbers using Recursion
    :param x:
    :param y:
    :return:
    """
    # this is check for cutting down the toatal
    # number of recusrive calls
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y - 1)


print(recursive_multiply(5, 300))
