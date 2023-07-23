class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    length = i - stack[-1]
                    max_len = max(max_len, length)
                else:
                    stack.append(i)
        return max_len




obj = Solution()
s = ")()())"
print(obj.longestValidParentheses(s))