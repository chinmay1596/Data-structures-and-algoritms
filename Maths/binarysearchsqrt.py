def square_root(x):
    """
    with float value
    :param x:
    :return:
    """
    start = 0
    end = x
    p = 2
    root = 0.0
    while start <= end:
        mid = (start + end) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            start = mid + 1
        else:
            end = mid - 1

    incr = 0.1
    for i in range(p):
        while root * root <= x:
            root += incr
        root -= incr
        incr /= 10
    return int(root)


# print(square_root(247776352))


def square_root1(x):
    """
    square root without float value
    :param x:
    :return:
    """
    start = 0
    end = x
    ans = -1
    while start <= end:
        mid = (start + end) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans


print(square_root(247776352))
