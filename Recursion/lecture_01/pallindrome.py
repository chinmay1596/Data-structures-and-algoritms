global summ
summ = 0


def reverse(n):
    """
    kunal 1 method
    :param n:
    :return:
    """
    if n == 0:
        return
    else:
        rem = n % 10
        global summ
        summ = summ * 10 + rem
        reverse(n // 10)
        return summ


def pallindrome(n):
    return n == reverse(n)


print(pallindrome(10))
