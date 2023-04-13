"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/
"""


class Solution:
    def solve(self, n, k):
        if n == 0:
            return 0
        return (self.solve(n - 1, k) + k) % n

    def findTheWinner(self, n: int, k: int) -> int:
        ans = self.solve(n, k) + 1
        return ans

obj = Solution()
print(obj.findTheWinner(5, 2))