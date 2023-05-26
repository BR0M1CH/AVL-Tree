import random


class Node:

    def __init__(self, data):
        self.left = self.right = None
        self.data = data
        self.balance = 0

    def addleft(self, data):
        self.left = Node(data)

    def addright(self, data):
        self.right = Node(data)

    def hasleft(self):
        if self.left != None:
            return True
        return False
    
    def hasright(self):
        if self.right != None:
            return True
        return False
    
    def balancing(self):

        if self.balance < -1:
            if self.left.balance == -1:
                buffer = self.left
                self.left = None
                buffer.right = self
                self = buffer
            elif self.left.balance == 1:
                buffer = self.left
                self.left = self.left.right
                buffer.right = None
                self.left.left = buffer
                buffer = self.left
                self.left = None
                buffer.right = self
                self = buffer
        elif self.balance > 1:
            if self.right.balance == 1:
                buffer = self.right
                self.right = None
                buffer.left = self
                self = buffer
            elif self.right.balance == -1:
                buffer = self.right
                self.right = self.right.left
                buffer.left = None
                self.right.right = buffer
                buffer = self.right
                self.right = None
                buffer.left = self
                self = buffer


class Tree:

    def __init__(self, data):   
        self.root = Node(data)
        self.size = 1
        self.currentNode = self.root      

    
    def add(self, data, **start):
        
        if start == self.root:
            self.currentNode = self.root

        if data == self.currentNode.data:
            return
   
        elif data < self.currentNode.data:
            if self.currentNode.hasleft():
                self.currentNode = self.currentNode.left
                self.add(data)
            else:
                self.currentNode.addleft(data)
                self.currentNode.balance -=1
                if self.currentNode.balance < -1:
                    self.currentNode.balancing()
      
        elif data > self.currentNode.data:
            if self.currentNode.hasright():
                self.currentNode = self.currentNode.right
                self.add(data)
            else:
                self.currentNode.addright(data)
                self.currentNode.balance+=1
                if self.currentNode.balance > 1:
                    self.currentNode.balancing()
        
    
    def find(self, data, **start):

        if start == self.root:
            self.currentNode = self.root

        if data < self.currentNode.data:
            if self.currentNode.hasleft():
                self.currentNode = self.currentNode.left
                self.find(data)
            else:
                self.currentNode = self.root
                return False
            
        elif data > self.currentNode.data:
            if self.currentNode.hasright():
                self.currentNode = self.currentNode.right
                self.find(data)
            else:
                self.currentNode = self.root
                return False
        
        elif data == self.currentNode.data:
            self.currentNode = self.root
            return True

    
    def show(self, node):
        if node.hasleft():
            self.show(node.left)
        print(node.data)
        if node.hasright():
            self.show(node.right)


        





t = Tree(10)
t.add(9, start=t.root)
print("1 added")
t.add(8, start=t.root)
print("2 added")
t.add(3, start=t.root)
print("3 added")
t.add(4, start=t.root)
print("4 added")
t.add(1, start=t.root)
print("1 added")
t.add(5, start=t.root)
print("5 added")
t.add(2, start=t.root)
print("2 added")
t.add(7, start=t.root)
print("7 added")
t.add(6, start=t.root)
print("6 added")
t.show(t.root)


