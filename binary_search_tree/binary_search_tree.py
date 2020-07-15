"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BSTNode(int(value))
        current = self
        if current.value is None:
            current = node
        else:
            while current != node:
                if current.value == node.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        current = current.right
                while node.value < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        current = current.left
                        break
                        
                while node.value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        current = current.right
                        break
                        



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        root = self
        unexplored = []
        if root:
            unexplored.append(root)
        current = unexplored[0]
        while unexplored and current.value != target:
            current = unexplored.pop(0)
            if current.left:
                unexplored.append(current.left)
            if current.right:
                unexplored.append(current.right)
        if current.value == target:
            return True
        else:
            return False
            
            


    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        while current.right != None:
            current = current.right
        return current.value
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        root = self
        unexplored = []
        if root:
            unexplored.append(root)
        current = unexplored[0]
        while unexplored:
            fn(current.value)
            current = unexplored.pop(0)
            if current.left:
                unexplored.append(current.left)
            if current.right:
                unexplored.append(current.right)
        fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
