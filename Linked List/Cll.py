class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.next = self.head
        self.tail = new_node

    def delete(self, val):
        temp_node = self.head
        if not temp_node:
            return

        if temp_node.data == val:
            self.head = self.head.next
            self.tail.next = self.head
            return

        while True:
            n = temp_node.next
            if n.data == val:
                temp_node.next = n.next
                return
            temp_node = temp_node.next
            if temp_node == self.head:
                break

    def display(self):
        node = self.head
        if node:
            while True:
                print(str(node.data) + ' -> ', end='')
                node = node.next
                if node == self.head:
                    break

    def cycle_length(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                temp_node = slow
                length = 0
                while True:
                    temp_node = temp_node.next
                    length += 1

                    if fast == temp_node:
                        return length
        return 0


cll = CircularLinkedList()
cll.insert(3)
cll.insert(4)
cll.insert(44)
cll.insert(23)
print(cll.cycle_length())
