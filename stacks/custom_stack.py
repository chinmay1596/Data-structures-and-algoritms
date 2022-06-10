class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * self.size
        self.top = -1

    def push(self, val):
        if self.top < self.size-1:
            self.top += 1
            self.arr[self.top] = val
            return val
        else:
            return 'stack overflow'

    def pop(self):
        if self.top > -1:
            var = self.arr[self.top]
            self.top -= 1
            return var
        else:
            return 'stack underflow'

    def peek(self):
        if self.top > -1:
            return self.arr[self.top]
        else:
            return 'stack empty'

    def is_empty(self):
        if self.top == -1:
            return True
        return False


st = Stack(5)
print(st.push(1))
print(st.push(2))
print(st.push(3))
print(st.push(4))
print(st.push(5))
print(st.push(6))
print(st.pop())
print(st.pop())
print(st.peek())
print(st.is_empty())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.is_empty())
