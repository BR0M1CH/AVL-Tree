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
                    if data == 5:
                        print(f"NODA = {node}")
                    return node, 2
                return node, 1
        
        elif data > node.data:
            if node.hasright():
                res = self.add(data, node.right, level+1)
                node.right = res[0]
                if res[1] == 2:
                    node.balance += 1
                    print(f"NODA = {node}")
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
            #newnode.right.balance = 1
            newnode.left.balance = 0
            print("left")
        else:
            newnode = node.right
            node.right = None
            newnode.left = node
            newnode.left.balance = 0
            newnode.balance = 0
            try:
                newnode.right.balance = 0
            except: pass
            print("noleft")
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
            #newnode.left.balance = -1
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
            print("noright")
        return newnode
        
        

    
    def big_left_rotate(self, node):
        newnode = node.copy()
        newnode.right = self.right_rotate(newnode.right)
        newnode = self.left_rotate(newnode)
        print("bigright")
        return newnode
    
    def big_right_rotate(self, node):
        newnode = node.copy()
        newnode.left = self.left_rotate(newnode.left)
        print(newnode)
        newnode = self.right_rotate(newnode)
        print(newnode)
        return newnode
    
    def balancing(self, noda) -> Node:
        # if noda is self.root:
        #     print(999999)
        #     print(noda.balance)
        #     print(noda.left.balance)
        #     print(noda.right.balance)
        # print(noda)
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

    


        


t = Tree(10)

t.add(1)
t.add(2)
t.add(3)
t.add(4)
t.add(5)
t.add(6)
t.add(7)
t.add(8)
t.add(9)
t.print()
# t.add(2)
# t.print()
# print("_"*30)
# t.add(5)
# t.print()
# print("_"*30)
# t.add(11)
# t.print()
# print("_"*30)
# t.add(7)
# t.print()
# print("_"*30)
# t.add(8)
# t.print()
# print("_"*30)
# t.add(13)
# t.print()
# print("_"*30)
# t.add(1)
# t.print()
# print("_"*30)
# t.add(6)
# t.print()
# print("_"*30)
# t.add(24)
# t.print()
# print("_"*30)