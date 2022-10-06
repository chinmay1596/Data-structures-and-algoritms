class MinStack:

    def __init__(self):
        self.item = []
        self.mini = None

    def push(self, val: int) -> None:
        if self.isEmpty():
            self.item.append(val)
            self.mini = val
        else:
            if val >= self.mini:
                self.item.append(val)
            else:
                new_val = ((2 * val) - self.mini)
                self.item.append(new_val)
                self.mini = val

    def pop(self) -> None:
        if self.isEmpty():
            return -1
        top_ele = self.item[-1]
        if top_ele > self.mini:
            self.item.pop()
        else:
            self.mini = ((2 * self.mini) - top_ele)
            self.item.pop()

    def top(self) -> int:
        if self.isEmpty():
            return -1
        top_ele = self.item[-1]
        if top_ele >= self.mini:
            return top_ele
        else:
            return self.mini

    def getMin(self) -> int:
        if self.isEmpty():
            return -1
        return self.mini

    def isEmpty(self):
        return len(self.item) == 0

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())