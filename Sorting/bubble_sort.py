def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(1, len(nums) - i):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums


print(bubble_sort([5, 3, 4, -21, 3, 2, 1, 1]))
