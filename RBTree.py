class Node(object):

    def __init__(self, data):
        self.data = data
        self.balance = 0
        self.left = self.right = None
        
    def copy(self):
        newnode = Node(self.data)
        newnode.left = self.left
        newnode.right = self.right
        newnode.balance = self.balance
        return newnode

    def addleft(self, data):
        self.left = Node(data)

    def addright(self, data):
        self.right = Node(data)

    
    def hasleft(self):
        if self.left==None:
            return False
        return True
    

    def hasright(self):
        if self.right==None:
            return False
        return True
    
    
    def __str__(self):
        a = str(self.data)
        if self.hasleft():
            a+=f", left: {self.left.data}"
        if self.hasright():
            a+=f", right: {self.right.data}"
        a+=f", balance: {self.balance}"
        return(a)
    
    def calc_height(self, level = 0):
        if self.hasleft():
            l = self.calc_height(self.left, level+1)
        
        
        


class Tree(object):

    bufferTree = None

    def __init__(self, data):  
        self.root = Node(data)


    def print(self, node=None):
        if node==None:
            node = self.root
        if node.hasleft():
            self.print(node = node.left)
        print(node)
        if node.hasright():
            self.print(node = node.right)


    def add(self, data, node=None, level = 0):
        if node == None: node = self.root
        if data == node.data: return node, 0
        
        if data < node.data:
            if node.hasleft():
                res = self.add(data, node.left, level+1)
                node.left = res[0]
                if res[1] == 2:
                    node.balance -= 1
                    if node.balance < -1:
                        if node is not self.root:
                            node = self.balancing(node)
                            return node, 1
                        else:
                            self.root = self.balancing(self.root)
                            return self.root, 1
                return node, res[1]
            else:
                node.addleft(data)
                if not node.hasright():
                    node.balance -= 1
                    return node, 2
                node.balance+=1
                return node, 1
        
        elif data > node.data:
            if node.hasright():
                res = self.add(data, node.right, level+1)
                node.right = res[0]
                if res[1] == 2:
                    node.balance += 1
                    if node.balance > 1:
                        if node is not self.root:
                            node = self.balancing(node)
                            return node, 1
                        else:
                            self.root = self.balancing(self.root)
                            return self.root, 1
                return node, res[1]
            else:
                node.addright(data)
                if not node.hasleft():
                    node.balance += 1
                    return node, 2
                node.balance -=1
                return node, 1
        
                

    def left_rotate(self, node):
        buffer = Node(node.data)
        buffer.right = node.right
        buffer.left = node.left 
        if node.right.hasleft():
            newnode = node.right
            node.right = newnode.left
            newnode.left = node
            newnode.balance = 0
            newnode.left.balance = 0
        else:
            newnode = node.right
            node.right = None
            newnode.left = node
            newnode.left.balance = 0
            newnode.balance = 0
            try:
                newnode.right.balance = 0
            except: pass
        return newnode
       
    
    def right_rotate(self, node):
        buffer = Node(node.data)
        buffer.right = node.right
        buffer.left = node.left 
        if node.left.hasright():
            newnode = node.left
            node.left = newnode.right
            newnode.right = node
            newnode.balance = 0
            newnode.right.balance = 0
        else:
            newnode = node.left
            node.left = None
            newnode.right = node
            try:
                newnode.left.balance = 0
            except: pass
            newnode.balance = 0
            newnode.right.balance = 0
        return newnode
        
        

    
    def big_left_rotate(self, node):
        newnode = node.copy()
        newnode.right = self.right_rotate(newnode.right)
        newnode = self.left_rotate(newnode)
        return newnode
    
    def big_right_rotate(self, node):
        newnode = node.copy()
        newnode.left = self.left_rotate(newnode.left)
        newnode = self.right_rotate(newnode)
        return newnode
    
    def balancing(self, noda) -> Node:
        if noda.balance > 1:
            if noda.right.balance == -1:
                newnode = self.big_left_rotate(noda)
            elif noda.right.balance == 1:
                newnode = self.left_rotate(noda)
        elif noda.balance < -1:
            if noda.left.balance == 1:
                newnode = self.big_right_rotate(noda)
            elif noda.left.balance == -1:
                newnode = self.right_rotate(noda)       
        return(newnode)
    

    def sum(self, other, node = None):
        if node == None:
            node = other.root
        if node.hasleft():
            self.sum(other, node.left)
        self.add(node.data)
        if node.hasright():
            self.sum(other, node.left)
        return self
    
    def check(self,data, node = None):
        if node == None:
            node = self.root
        if data == node.data:
            return True
        if data < node.data:
            if node.hasleft():
                return self.check(data, node.left)
            return False
        if data > node.data:
            if node.hasright():
                return self.check(data, node.right)
            return False
        return False
    
    def modify_check(self, other, node = None):
        if node == None:
            node = self.root
        if other.check(node.data):
            return True, node.data
        if node.hasleft():
            res = self.modify_check(other, node.left)
            try: 
                if res[0]:
                    return res
            except: pass
        if node.hasright():
            res = self.modify_check(other, node.right)
            try: 
                if res[0] == True:
                    return res
            except: pass


    def helper_conuction(self, other, node = None):
        if node == None:
            node = self.root
        if other.check(node.data):
            Tree.bufferTree.add(node.data)
        if node.hasleft():
            self.helper_conuction(other, node.left)
        if node.hasright():
            self.helper_conuction(other, node.right)
        
            


    
    def conuction(self, other):
        Tree.bufferTree = None
        res = self.modify_check(other)
        try: 
            if res[0] == True:
                Tree.bufferTree = Tree(res[1])
                self.helper_conuction(other)
                return Tree.bufferTree
        except:
            return None
        
        
        



            
            
        

        
        



    


        


t = Tree(10)
b = Tree(12)

t.add(1)
t.add(5)
t.add(11)
t.add(15)
t.add(8)
t.add(6)
t.print()
print("-"*20)

b.add(3)
b.add(4)
b.add(12)
b.add(15)
#b.print()
b.add(5)
b.add(6)
b.print()
print("-"*20)


print("КОНЪЮНКЦИЯ")
c = t.conuction(b)
if isinstance(c, Tree):
    c.print()
else:
    print(None)

