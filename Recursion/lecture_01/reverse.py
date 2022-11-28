import math
#
#
def reverse_number(n):
    if n == 0:
        return
    else:
        print((n % 10), end='')
        reverse_number(n // 10)


# reverse_number(1824)


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


# reverse(1234)
# print(summ)


class Reverse:
    def reverse2(self, n):
        """
        sometimes you might need some additional variables in the argument in that case make another function
        :return:
        """
        digits = round(math.log10(n) + 1)
        return self.helper(n, digits)

    def helper(self, n, digits):
        if n % 10 == n:
            return n
        rem = n % 10
        return rem * round(math.pow(10, digits - 1)) + self.helper(n // 10, digits - 1)


a = Reverse()
print(a.reverse2(1234))
