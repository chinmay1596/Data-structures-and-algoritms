from copy import copy, deepcopy



class SubsetRecursive:

    def solve(self, nums, index, output, ans):
        if index == len(nums):
            ans.append(output)
            return

        # exclude
        output = output.copy()
        self.solve(nums, index + 1, output, ans)

        # include
        element = nums[index]
        output = output.copy()
        output.append(element)
        self.solve(nums, index + 1, output, ans)

    def solve1(self, nums, index, output):
        l = []
        if index == len(nums):
            l.append(output)
            return l

        # exclude
        output = output.copy()
        a = self.solve1(nums, index + 1, output)

        # include
        element = nums[index]
        output = output.copy()
        output.append(element)
        b = self.solve1(nums, index + 1, output)
        a.extend(b)
        return a

    def subset1(self, nums):
        output = []
        index = 0
        return self.solve1(nums, index, output)

    def subset(self, nums):
        ans = []
        output = []
        index = 0
        self.solve(nums, index, output, ans)
        return ans


obj = SubsetRecursive()
nums = [0, 0, 0]
print(obj.subset(nums))
