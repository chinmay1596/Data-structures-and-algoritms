# nums = [15, 18, 2, 3, 6, 12]
nums = [66, 67, 7, 10, 14, 19, 27, 33, 36, 40, 44, 54, 60]
target = 3


class Solution:
    # def binary_search(self, low, high):
    #     low = low
    #     high = high
    #
    #     while low <= high:
    #         mid = (low + high) // 2
    #
    #         if nums[mid] == target:
    #             return True
    #         elif target > nums[mid]:
    #             low = mid + 1
    #         elif target < nums[mid]:
    #             high = mid - 1
    #     return False
    #
    # def search(self, nums, target):
    #     pivot = self.find_pivot(nums, target)
    #     if not pivot:
    #         return self.binary_search(low=0, high=len(nums) - 1)
    #
    #     if nums[pivot] == target:
    #         return pivot
    #     if target >= nums[0]:
    #         return self.binary_search(low=0, high=pivot - 1)
    #
    #     return self.binary_search(low=pivot + 1, high=len(nums) - 1)

    def find_pivot(self, nums):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if high > mid and nums[mid] > nums[mid + 1]:
                return mid+1
            if mid > low and nums[mid] < nums[mid - 1]:
                return (mid - 1)+1
            if nums[low] >= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1+1


a = Solution()
print(a.find_pivot(nums))
