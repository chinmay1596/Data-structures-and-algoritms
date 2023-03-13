class Solution:

    def solve(self, t, index, output, ans=[]):
        if index == len(t):
            ans.append(output)
            return ans

        self.solve(t, index + 1, output + t[index])
        self.solve(t, index + 1, output)
        return ans

    def isSubsequence(self, s: str, t: str) -> bool:
        ans = self.solve(t, 0, '')
        # print(ans)
        for i in ans:
            if i == s:
                return True
        return False


obj = Solution()
s = 'b'
t = 'c'
print(obj.isSubsequence(s, t))
