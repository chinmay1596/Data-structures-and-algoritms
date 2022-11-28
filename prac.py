def minSwaps(nums):
    count = 0
    d = []
    for i in range(len(nums)):
        d.append([nums[i], i])
    d.sort()

    j = 0
    while j < len(d):
        if j != d[j][1]:
            a = d[j][1]
            d[j], d[a] = d[a], d[j]
            count += 1
        else:
            j += 1
    return count


print(minSwaps([13, 1, 5, 3, 6, 11, 10]))
