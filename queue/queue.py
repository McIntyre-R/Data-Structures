"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
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
    
    def pop_tail(self):
        if(self.head):
            current = self.head
            while(current.next != self.tail):
                current = current.next
            self.tail = current
            return current.next.value








class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = len(self.storage)

    def dequeue(self):
        if(self.size == 0):
            pass
        else:
            self.size -= 1
            return self.storage.pop_head()
            

