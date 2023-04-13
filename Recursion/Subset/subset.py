from copy import copy, deepcopy


class SubsetIterative:
    sub = [1, 2, 3]
    sub1 = [1, 2, 2]

    @classmethod
    def subset_array(cls):
        arr = []
        arr.append([])
        for i in cls.sub:
            internal_array = deepcopy(arr)
            for j in range(len(internal_array)):
                internal_array[j].append(i)
            arr.extend(internal_array)

        return arr

    def duplicate_subset(self):
        SubsetIterative.sub1.sort()
        arr = []
        arr.append([])
        start = 0
        end = 0
        for i in range(len(SubsetIterative.sub1)):
            internal_array = deepcopy(arr)
            if i > 0 and SubsetIterative.sub1[i] == SubsetIterative.sub1[i - 1]:
                start = end + 1
                end = len(arr) - 1
            else:
                end = len(arr) - 1
            for j in range(start, end + 1):
                internal_array[j].append(SubsetIterative.sub1[i])
            arr.extend(internal_array[start:end + 1])
        return arr


# obj = SubsetIterative()
# print(obj.subset_array())


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
print(obj.subset1([0, 0, 0]))
