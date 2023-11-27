class Queue:

    def __init__(self, size):
        self.arr = [None] * size
        self.rear = 0
        self.front = 0
        self.size = size

    def push(self, val:int):
        pass