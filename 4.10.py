class node:
    def __init__(self,name:int):
        self.name = name
        self.leftChild = None
        self.rightChild = None
        self.front = None
        self.behind = None

class Tree:
    def __init__(self,root:node):
        self.root = root

class Queue:
    def __init__(self):
        self.first = None
        self.last = self.first
    def enqueue(self,node):
        if(self.first == None):
            self.first = node
            self.first.front = None
            self.first.behind = None
            self.last = self.first
        else:
            if(self.first == self.last):
                self.last = node
                self.last.front = self.first
                self.last.behind = None
                self.first.behind = self.last
            else:
                tmp = self.last
                self.last = node
                self.last.front = tmp
                self.last.front.behind = self.last
    def dequeue(self):
        if(self.first==None):
            print("error")
        elif(self.first == self.last):
            tmp = self.first
            self.first = None
            self.last = None
            return tmp 
        else:
            tmp = self.first
            self.first = self.first.behind
            self.first.front = None
            return tmp
    def peek(self):
        return self.first
    def isEmpty(self):
        return self.last == None and self.first == None

    
    ##no link to paretns: DFS

def checkSubtree(T1:Tree,T2:Tree) -> bool:
    root = T1.root
    return DFS(T1,root.leftChild,T2.root) or DFS(T1,root.rightChild,T2.root)

def DFS(T1:Tree,root:node,searched:node):
    if(root == searched):
        return True
    elif(not (root.leftChild and root.rightChild)):
        if(root.leftChild):
            DFS(T1,root.leftChild,searched)
        elif(root.rightChild):
            DFS(T1,root.rightChild,searched)
        else:
            return False
    else:
        return DFS(T1,root.leftChild,searched) or DFS(T1,root.rightChild,searched)

a = node(4)
b = node(2)
c = node(6)
d = node(1)
e = node(3)
f = node(5)
g = node(7)
j = node(8)
a.leftChild = b
b.leftChild = d
a.rightChild = c
b.rightChild = e
c.leftChild = f
c.rightChild = g
g.rightChild = j
h = Tree(a)
v = Tree(g)
print(checkSubtree(h,v))