# User function Template for python3


class Solution:
    def maxArea(self, M):
        area = -1
        arr = M[0]
        mah = Mah()
        for row in range(len(M)):
            if row > 0:
                for col in range(len(M[0])):
                    if M[row][col] == 0:
                        arr[col] = 0
                    else:
                        arr[col] += M[row][col]
            new_area = mah.largestRectangleArea(arr)
            area = max(area, new_area)
        return area


class Mah:
    def prev_smaller_element(self, heights, n):
        arr = [0] * n
        stack = Stack()
        stack.push(-1)
        for i in range(len(heights)):
            while stack.peek() != -1 and heights[stack.peek()] >= heights[i]:
                stack.pop()
            arr[i] = stack.peek()
            stack.push(i)
        return arr

    def next_smaller_element(self, heights, n):
        arr = [0] * n
        stack = Stack()
        stack.push(-1)
        for i in range(len(heights) - 1, -1, -1):
            while stack.peek() != -1 and heights[stack.peek()] >= heights[i]:
                stack.pop()
            arr[i] = stack.peek()
            stack.push(i)
        return arr

    def largestRectangleArea(self, heights):
        n = len(heights)
        area = -1
        prev_num = self.prev_smaller_element(heights, n)
        next_num = self.next_smaller_element(heights, n)

        for i in range(len(heights)):
            l = heights[i]
            if next_num[i] == -1:
                next_num[i] = n
            b = next_num[i] - prev_num[i] - 1
            new_area = l * b
            area = max(area, new_area)
        return area


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()


M = [[1, 0, 0, 0],
     [0, 1, 1, 1],
     [0, 0, 1, 0],
     [0, 1, 1, 1]]

obj = Solution()
print(obj.maxArea(M))
