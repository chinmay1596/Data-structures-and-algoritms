"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        parent = self.kthGrammar(n - 1, k // 2 + k % 2)

        if parent == 0:
            if k % 2 == 0:
                return 1
            else:
                return 0
        else:
            if k % 2 == 0:
                return 0
            else:
                return 1


obj = Solution()
print(obj.kthGrammar(2, 1))
