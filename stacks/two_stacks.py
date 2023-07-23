
class TwoStack:
    def __init__(self, size) -> None:
        self.arr = [None]*size
        self.size = size
        self.top1 = -1
        self.top2 = size


    def push1(self, val):
        if self.top2 - self.top1 == 1:
            return "Stack overflow"
        
        self.top1+=1
        self.arr[self.top1] = val
    

    def pop1(self):
        if self.top1 == -1:
            return "Stack emppty"
        self.arr[self.top1] = None
        self.top1-=1
    

    def push2(self, val):
        if self.top2 - self.top1 == 1:
            return "Stack overflow"
        
        self.top2-=1
        self.arr[self.top2] = val

    def pop2(self):
        if self.top2 == self.size:
            return "Stack emppty"
        self.arr[self.top2] = None
        self.top2+=1
    




if __name__ == "__main__":
    obj = TwoStack(5)
    # print(obj.arr)
    
    obj.push1(1)
    obj.push1(2)
    obj.push1(3)
    obj.push2(5)
    obj.push2(6)
    print(obj.push1(8))
    