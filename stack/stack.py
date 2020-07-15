"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head


    def __len__(self):
        return self.getLength()
    
    def getLength(self):
        if(self.head):
            current = self.head
            i = 0
            while(current):
                current = current.next
                i += 1
            return i
        else:
            return 0

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
            return current.value






class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()
    
    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.add_as_head(value)
        self.size = len(self.storage)


    def pop(self):
        if(self.size == 0):
            pass
        else:
            self.size -= 1
            return self.storage.pop_head()
            

