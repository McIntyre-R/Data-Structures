class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head


    def __len__(self):
        if(self.head):
            current = self.head
            i = 1
            while(current):
                current = current.next
                i += 1
            return i

    def add_to_tail(self, value):
        newNode = Node(value) 
        if(self.head):
            current = self.tail
            while(current.next):
                current = current.next
            current.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode

    def add_as_head(self, value):
        newNode = Node(value) 
        if(self.head):
            current = self.head
            newNode.next = current
            self.head = newNode

        else:
            self.head = newNode
            self.tail = newNode 


    def pop_head(self):
        if(self.head):
            current = self.head
            self.head = current.next
            return current





LL = LinkedList()
LL.add_to_tail(3)
print('test 1')
LL.printLL()
LL.add_to_tail(4)
print('test 2')
LL.printLL()
LL.add_to_tail(5)
print('test 3')
LL.printLL()

