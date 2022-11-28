class Permutations:

    def permutations(self, p, up):
        if len(up) == 0:
            print(p)
            return

        first_char = up[0]

        for i in range(len(p) + 1):
            f = p[0:i]
            s = p[i: len(p)]
            self.permutations(f + first_char + s, up[1:])

    def perm_array(self, p, up):
        l = []
        if len(up) == 0:
            l.append(p)
            return l

        first_char = up[0]
        ans = []

        for i in range(len(p) + 1):
            f = p[0:i]
            s = p[i: len(p)]
            ans.extend(self.perm_array(f + first_char + s, up[1:]))

        return ans

    def permutations_count(self, p, up):
        if len(up) == 0:
            return 1

        count = 0
        first_char = up[0]
        for i in range(len(p) + 1):
            f = p[0:i]
            s = p[i: len(p)]
            count = count + self.permutations_count(f + first_char + s, up[1:])
        return count

    def permutations1(self, nums, index):
        ans = []
        if index == len(nums):
            ans.append(nums)
            return ans

        for j in range(index, len(nums)):
            nums[index], nums[j] = nums[j], nums[index]
            nums = nums.copy()
            ans.extend(self.permutations1(nums, index + 1))
            # backtrack
            nums[index], nums[j] = nums[j], nums[index]
        return ans

    def permutations_count1(self, nums, index):
        count = 0
        if index == len(nums):
            count += 1
            return count

        for j in range(index, len(nums)):
            nums[index], nums[j] = nums[j], nums[index]
            nums = nums.copy()
            count = count + len(self.permutations1(nums, index + 1))
            nums[index], nums[j] = nums[j], nums[index]
        return count


obj = Permutations()
# obj.permutations('', 'abc')
# print(obj.perm_array('', 'abc'))
print(obj.permutations_count1([1, 2, 3], 0))
