class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def printlist(self):
        temp_node = self.head
        while temp_node:
            print(str(temp_node.data) + " -> ", end='')
            temp_node = temp_node.next
        print("END")

    def insert_at_head(self, val: int):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self.head
        new_node.next = self.head
        self.head = new_node
        return self.head

    def insert_at_tail(self, val: int):
        new_node = Node(val)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
            return self.tail
        self.tail.next = new_node
        self.tail = new_node
        return self.tail

    def insert_at_position(self, pos, val):
        if not self.head:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            return
        if pos == 0:
            self.insert_at_head(val)
            return

        temp = self.head
        count = 1
        while count < pos:
            temp = temp.next
            count += 1



    # def insert_first(self, val):
    #     new_node = Node(val)
    #     # if we are creating first node then new_node.next = None because self.head initially is pointing to None
    #     new_node.next = self.head
    #     self.head = new_node
    #     if not self.tail:  # if tail is at null
    #         self.tail = self.head
    #
    #     self.size += 1
    #
    # def insert(self, val, index):
    #     if index == 0:
    #         self.insert_first(val)
    #         return
    #     if index == self.size:
    #         self.insert_last(val)
    #         return
    #     temp = self.head
    #     for i in range(1, index):
    #         temp = temp.next
    #
    #     new_node = Node(val, temp.next)
    #     temp.next = new_node
    #     self.size += 1
    #
    # def insert_recursive(self, val, index):
    #     self.head = self.insert_rec(val, index, self.head)
    #
    # def insert_rec(self, val, index, node):
    #     if index == 0:
    #         new_node = Node(val, node)
    #         self.size += 1
    #         return new_node
    #     index -= 1
    #     node.next = self.insert_rec(val, index, node.next)
    #     return node
    #
    # def get_node(self, index):
    #     temp = self.head
    #     for i in range(index):
    #         temp = temp.next
    #     return temp
    #
    # def delete_last(self):
    #     if self.size <= 1:
    #         self.delete_first()
    #         return
    #     node = self.get_node(self.size - 2)
    #     val = self.tail.data
    #     self.tail = node
    #     node.next = None
    #     self.size -= 1
    #     return val
    #
    # def delete_first(self):
    #     val = self.head.data
    #     self.head = self.head.next
    #     if not self.head:
    #         self.tail = None
    #     self.size -= 1
    #     return val
    #
    # def delete(self, index):
    #     if index == 0:
    #         self.delete_first()
    #         return
    #     if index == self.size - 1:
    #         self.delete_last()
    #         return
    #     temp = self.get_node(index - 1)
    #     next_node = temp.next
    #     temp.next = temp.next.next
    #     next_node = None
    #     self.size -= 1
    #
    # def get_head(self):
    #     return self.head
    #
    # def reverse_recursive(self, node):
    #     if node == self.tail:
    #         self.head = self.tail
    #         return
    #
    #     self.reverse_recursive(node.next)
    #     self.tail.next = node
    #     self.tail = node
    #     self.tail.next = None
    #
    # def reverse_iterative(self):
    #     curr_node = self.head
    #     prev = None
    #
    #     while curr_node:
    #         temp = curr_node.next
    #         curr_node.next = prev
    #         prev = curr_node
    #         curr_node = temp
    #
    #     return prev


llist = LinkedList()
llist.insert_at_head(2)
llist.insert_at_head(1)
llist.insert_at_tail(1)
llist.insert_at_tail(2)
llist.insert_at_tail(3)

llist.printlist()
