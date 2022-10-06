class NQueue:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = self.next_arr()
        self.freespot = 0
        self.arr = [None] * n

    def enqueue(self, val, qn):
        # overflow condition
        if self.freespot == -1:
            print("No empty space present")
            return

        # find first free index
        index = self.freespot

        # update freespot
        self.freespot = self.next[index]

        # check wether first element
        if self.front[qn - 1] == -1:
            self.front[qn - 1] = index
        else:
            # link new element to prev element
            self.next[self.rear[qn - 1]] = index

        # update next
        self.next[index] = -1

        # update rear
        self.rear[qn - 1] = index

        self.arr[index] = val

    def dequeue(self, qn):
        if self.front[qn - 1] == -1:
            print("queue is empty")
            return

        # find index to pop
        index = self.front[qn - 1]

        # front ko age badhao
        self.front[qn - 1] = self.next[index]

        # free_slots ko manage karo
        self.next[index] = self.freespot
        self.freespot = index
        return self.arr[index]

    def next_arr(self):
        l = []
        for i in range(self.n):
            l.append(i + 1)
        l[self.n - 1] = -1
        return l
