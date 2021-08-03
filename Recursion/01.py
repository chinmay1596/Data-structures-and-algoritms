"""
we have to find no of digits given number n
"""


def digits(n):
    if n == 1:
        return 1
    smalldigit = digits(n // 10)  # n//10 will remove the last integer of the digit
    ans = smalldigit + 1
    return ans


print(digits(1675445))


def num(n):
    """
    print numbers from 1 to n
    :param n:
    :return:
    """
    if n == 0:
        return
    print(n)
    smalldigit = num(n - 1)


num(5)



def inum(n):

    if n == 0:
        return
    smalldigit = inum(n-1)
    print(n)

inum(5)