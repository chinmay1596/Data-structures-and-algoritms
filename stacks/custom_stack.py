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


st = Stack()
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

