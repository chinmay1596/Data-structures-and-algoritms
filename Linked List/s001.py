class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        start = self.head
        while start:
            print(start.data)
            start = start.next

    def append(self, val):
        start = self.head
        while start:
            if start.next is None:
                start.next = Node(val)
                break
            else:
                start = start.next

    def append_after(self, after, val):
        start = self.head
        while start:
            if start.data == after:
                next_node = start.next
                start.next = None
                start.next = Node(val)
                start.next.next = next_node
                start = start.next
            else:
                start = start.next

    def delete(self, val):
        pass


llist = LinkedList()
llist.head = Node(1)
llist.head.next = Node(2)
llist.head.next.next = Node(3)


llist.append(4)
llist.append(5)
llist.append_after(2, 9)
llist.printlist()