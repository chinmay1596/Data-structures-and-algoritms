class Solution:
    def search(self, nums, target):
        pivot = self.find_pivot(nums)
        if pivot == -1:
            return self.binary_search(nums, target, low=0, high=len(nums) - 1)

        if nums[pivot] == target:
            return True
        if target >= nums[0]:
            return self.binary_search(nums, target, low=0, high=pivot - 1)

        return self.binary_search(nums, target, low=pivot + 1, high=len(nums) - 1)

    def find_pivot(self, nums):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if high > mid and nums[mid] > nums[mid + 1]:
                return mid
            if mid > low and nums[mid] < nums[mid - 1]:
                return mid - 1
            # if elements at low, middle and high are equal just skip them
            if nums[mid] == nums[low] and nums[mid] == nums[high]:
                # skip the duplicates
                # NOTE: what if the low and high were the pivot?
                # check if low is pivot
                if low < mid and nums[low] > nums[low + 1]:
                    return low
                low += 1
                # check if high is pivot
                if high > mid and nums[high] < nums[high - 1]:
                    return high - 1
                high -= 1
            # now check in left and right array just as we did above
            # above we check for if all low, high and mid are same and if not now check simply what we will do oin simple roated binary search keeping in mind the duplicate elements in the array
            elif nums[low] < nums[mid] or (nums[low] == nums[mid] and nums[high] < nums[mid]):
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def binary_search(self, nums, target, low, high):
        low = low
        high = high

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True
            elif target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
        return False


a = Solution()
print(a.search([3, 1], 3))
