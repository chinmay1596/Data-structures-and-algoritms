nums = [7, 2, 5, 10, 8]
m = 2


def split_array():
    start = max(nums)
    end = sum(nums)

    while start < end:
        mid = (start + end) // 2

        s = 0
        pieces = 1
        for i in range(len(nums)):
            if s + nums[i] > mid:
                s = nums[i]
                pieces += 1
            else:
                s += nums[i]
        if pieces > m:
            start = mid+1
        else:
            end = mid
    return end

print(split_array())