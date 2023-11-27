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

    def insert_at_head(self, val):

        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        # purane node ka prev new node par ayega
        self.head.prev = new_node
        self.head = new_node

    def insert_at_tail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_at_pos(self, pos, val):
        curr_node = self.head
        count = 0
        while curr_node and pos - 1 != count:
            curr_node = curr_node.next
            count += 1

        new_node = Node(val)
        next_node = curr_node.next
        curr_node.next = new_node
        new_node.prev = curr_node
        new_node.next = next_node
        next_node.prev = new_node

    def delete_at_head(self):
        temp = self.head
        next_node = temp.next
        temp.next = None
        next_node.prev = None
        self.head = next_node
        del temp

    def delete_at_tail(self):
        temp = self.tail
        prev_node = temp.prev
        temp.prev = None
        prev_node.next = None
        self.tail = prev_node
        del temp

    def delete_at_pos(self, pos):
        temp = self.head
        count = 0
        while temp and pos != count:
            temp = temp.next
            count+=1
        next_node = temp.next
        curr_node = temp
        prev_node = temp.prev

        prev_node.next = curr_node.next
        next_node.prev = curr_node.prev
        curr_node.next = None
        curr_node.prev = None
        del curr_node




dll = DoublyLinkedList()
dll.insert_at_head(20)
dll.insert_at_head(10)
dll.insert_at_head(5)
dll.insert_at_tail(30)
dll.insert_at_tail(40)
dll.insert_at_pos(2, 15)
dll.delete_at_head()
dll.delete_at_tail()
dll.delete_at_pos(2)
dll.display()
