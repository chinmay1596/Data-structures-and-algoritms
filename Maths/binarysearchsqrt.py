def square_root(x):
    """
    with float value
    :param x:
    :return:
    """
    start = 0
    end = x
    precision_value = 3
    res = 0.0
    while start <= end:
        mid = (start + end) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            res = mid
            start = mid + 1
        else:
            end = mid - 1

    incr = 0.1
    for i in range(precision_value):
        while res * res <= x:
            res += incr
        # since it has gone up the x value
        # we need to come back,so we are decrementing
        res -= incr
        # this increment is based on precision value
        # so if we divide the increment by 10, it will be 0.01
        # since we asked for three precision value
        incr /= 10
    return round(res, precision_value)


print(square_root(40))

# def square_root1(x):
#     """
#     square root without float value
#     :param x:
#     :return:
#     """
#     start = 0
#     end = x
#     ans = -1
#     while start <= end:
#         mid = (start + end) // 2
#
#         if mid * mid == x:
#             return mid
#         elif mid * mid < x:
#             ans = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return ans
#
#
# print(square_root(247776352))
