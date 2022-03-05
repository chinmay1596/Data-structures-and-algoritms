class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def display(self):
        temp = self.head
        while temp:
            print(str(temp.data) + " -> ", end='')
            temp = temp.next
        print("END")

    def display_rev(self):
        temp = self.tail
        while temp:
            print(str(temp.data) + " <- ", end='')
            temp = temp.prev
        print("START")

    def insert_last(self, val):
        new_node = Node(val)
        new_node.next = None
        if not self.head:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last


    def insert_first(self, val):
        new_node = Node(val)
        new_node.next = self.head
        new_node.prev = None
        # to check if head is not at null otherwise it will give null pointer error
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = self.head
        self.size += 1


dll = DoublyLinkedList()
dll.insert_first(1)
dll.insert_first(2)
dll.insert_first(3)
dll.insert_last(100)
dll.display()
