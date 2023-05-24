import random


class Node:

    
    def __init__(self, data, parent):
        self.data = data
        self.left = self.right = None
        self.parent = parent

    
    def hasleft(self):
        return(self.left)
    
    
    def hasright(self):
        return(self.right)

class Tree:

    currentNode = None

    
    def __init__(self, data):
        self.root = Node(data, None)
        self.currentNode = self.root

    
    def put(self, data):
            
            if data < self.currentNode.data:
                if self.currentNode.hasleft():
                    self.currentNode = self.currentNode.left
                    self.put(data)
                else:
                    self.currentNode.left = Node(data, self.currentNode)
                    self.currentNode = self.root
                    return
                      
            elif data > self.currentNode.data:
                if self.currentNode.hasright():
                    self.currentNode = self.currentNode.right
                    self.put(data)
                else:
                    self.currentNode.right = Node(data, self.currentNode)
                    self.currentNode = self.root
                    return
            
            elif data == self.currentNode.data:
                self.currentNode = self.root
                print("This num already in tree")
                return

    
    def find(self, data):


        if data < self.currentNode.data:
            if self.currentNode.hasleft():
                self.currentNode = self.currentNode.left
            else:
                self.currentNode = self.root
                return False
        
        elif data > self.currentNode.data:
            if self.currentNode.hasright():
                self.currentNode = self.currentNode.right
            else:
                self.currentNode = self.root
                return False
                

        elif data == self.currentNode.data:
            self.currentNode = self.root
            return True
        

    def treeprint(self):
        pass

        
            
        

if __name__ == "__main__":
    
    rbtree = Tree(50)
    for i in range(20):
        a = random.randint(0,100)
        print(a)
        rbtree.put(a)
    rbtree.treeprint()
