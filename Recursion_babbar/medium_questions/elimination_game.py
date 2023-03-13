"""
https://leetcode.com/problems/elimination-game/
"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return n
        return 2 * (1 + n // 2 - self.lastRemaining(n // 2))
