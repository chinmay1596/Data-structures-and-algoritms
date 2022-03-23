class Solution:
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        while True:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
            if slow == fast:
                break
        if slow == 1:
            return True
        return False

    def square(self, n):
        square_sum = 0
        while n > 0:
            digit = n % 10
            square_sum += digit * digit
            n = n // 10
        return square_sum


obj = Solution()
print(obj.isHappy(19))