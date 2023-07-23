class Solution():

    def checkRedundancy(self, s):
        stack = []

        for i in s:
            operator_present = False
            if not i == ')':
                stack.append(i)
            else:
                while len(stack) > 0:
                    temp = stack.pop()
                    if temp in ['+', '-', '*', '/']:
                        operator_present = True
                    if temp == '(':
                        break
                if not operator_present:
                    return True
        return False


obj = Solution()
s = "((a+b))"
print(obj.checkRedundancy(s))
