def find_max(nums, start, end):
    index = start
    for i in range(start, end + 1):
        if nums[i] > nums[index]:
            index = i
    return index


def selection_sort(nums):
    for i in range(len(nums)):
        last = len(nums) - i - 1
        max_index = find_max(nums, 0, last)
        nums[max_index], nums[last] = nums[last], nums[max_index]
    return nums


print(selection_sort([-1, -9, 7, 8, 0]))
