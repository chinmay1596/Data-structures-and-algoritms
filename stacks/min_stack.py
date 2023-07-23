class MinStack:

    def __init__(self):
        self.arr = []
        

    def push(self, val: int) -> None:
        if len(self.arr) == 0:
            self.arr.append((val, val))
        else:
            top = self.arr[-1]
            min_ele = min(val, top[1])
            self.arr.append((val, min_ele))



    def pop(self) -> None:
        temp = self.arr.pop()
        

    def top(self) -> int:
        return self.arr[-1][0]
        

    def getMin(self) -> int:
        return self.arr[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()