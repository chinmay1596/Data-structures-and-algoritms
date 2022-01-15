def countsetbit(n):
    count = 0

    # while n > 0:
    #     last = n & 1
    #     if last == 1:
    #         count += 1
    #     n = n >> 1
    # return count

    while n > 0:
        count+=1
        n = n & (n-1)
    return count


print(countsetbit(9))
