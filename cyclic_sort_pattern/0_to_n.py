nums = [4, 3, 2, 7, 8, 2, 3, 1]


def o_to_n():
    i = 0
    while i <= len(nums) - 1:
        correct = nums[i] -1
        if i == correct or nums[i] == len(nums):
            i += 1
        else:
            nums[i], nums[correct] = nums[correct], nums[i]
    l = []
    for j in range(0, len(nums)):
        if nums[j] != j:
            l.append(j)
    if len(l) > 0:
        return l
    else:
        return len(nums)


print(o_to_n())
