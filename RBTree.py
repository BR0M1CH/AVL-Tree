import random


class Node:

    def __init__(self, data):
        self.left = self.right = None
        self.data = data

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
    

class Tree:

    def __init__(self, data):   
        self.root = Node(data)
        self.size = 1
        self.currentNode = self.root

    def add(self, data):
        
        if data < self.currentNode.data:
            if self.currentNode.hasleft():
                self.currentNode = self.currentNode.left
                self.add(data)
            else:
                self.currentNode.addleft(data)
                self.size += 1
                self.currentNode = self.root
        
        elif data > self.currentNode.data:
            if self.currentNode.hasright():
                self.currentNode = self.currentNode.right
                self.add(data)
            else:
                self.currentNode.addright(data)
                self.size += 1
                self.currentNode = self.root

    
    def find(self, data):
        if data < self.currentNode.data:
            if self.currentNode.hasleft():
                self.currentNode = self.currentNode.left
                self.find(self, data)
            else:
                self.currentNode = self.root
                return False
            
        elif data > self.currentNode.data:
            if self.currentNode.hasright():
                self.currentNode = self.currentNode.right
                self.find(self, data)
            else:
                self.currentNode = self.root
                return False
        
        elif data == self.currentNode.data:
            self.currentNode = self.root
            return True

    
    def show(self, node):
        print(node.data)
        if node.hasleft():
            self.show(node.left)
        if node.hasright():
            self.show(node.right)



t = Tree(10)
t.add(5)
print("5 added")
t.add(2)
print("2 added")
t.add(4)
print("4 added")
t.add(3)
print("3 added")
t.add(15)
print("15 added")
t.add(16)
print("16 added")
t.add(19)
print("19 added")
t.add(12)
print("12 added")
t.add(10)
print("10 added")
t.show(t.root)
