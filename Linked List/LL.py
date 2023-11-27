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
    
    def find_length(self, head:Node):
        temp = head
        count = 0
        while temp:
            count+=1
            temp = temp.next
        return count

    def insert_at_position(self, pos, val):
        if not self.head:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            return
        if pos == 0:
            self.insert_at_head(val)
            return
        
        length = self.find_length(self.head)

        if pos >= length:
            self.insert_at_tail(val)
            return

        prev = self.head
        index = 1
        while index < pos:
            prev = prev.next
            index += 1
        curr = prev.next
        new_node = Node(val)
        prev.next = new_node
        new_node.next = curr

    def delete(self, pos):
        if not self.head:
            return "ll not present"
        
        if pos == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            del temp
            return

        length = self.find_length(self.head)

        if pos > length-1:
            print("Invalid position")
            return

        prev = self.head
        index = 1
        while index < pos:
            prev = prev.next
            index+=1
        
        curr = prev.next
        prev.next = curr.next
        curr.next = None
        del curr


    


llist = LinkedList()
llist.insert_at_head(1)
llist.insert_at_tail(2)
llist.insert_at_tail(2)
llist.insert_at_tail(1)
llist.insert_at_tail(2)
llist.insert_at_tail(0)
llist.insert_at_tail(2)
llist.insert_at_tail(2)

llist.printlist()
