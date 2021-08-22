class node:
    def __init__(self,name:int):
        self.name = name
        self.leftChild = None
        self.rightChild = None
        self.next = None
        self.parent = None

class Tree:
    def __init__(self,root:node):
        self.root = root
    def printTree(self,root,text,parent):
        if(root == None):
            return
        print(root.name,text,parent)
        self.printTree(root.leftChild,"left Child of",root.name)
        self.printTree(root.rightChild,"right Child of",root.name)

def nextNode(tree:Tree,node:node):
    if(node.rightChild):
        tmp = node.rightChild
        while(tmp.leftChild != None):
            tmp = tmp.leftChild
        return tmp
    elif(node.parent and node == node.parent.leftChild):
        return node.parent
    elif(node.parent and node == node.parent.rightChild):
        tmp = node.parent
        while(tmp.parent and tmp != tmp.parent.leftChild):
            tmp = tmp.parent
        return tmp.parent
    return None
   

a = node(4)
b = node(2)
c = node(6)
d = node(1)
e = node(3)
f = node(5)
g = node(7)
a.leftChild = b
b.parent = a
b.leftChild = d
d.parent = b
a.rightChild = c
c.parent = a
b.rightChild = e
e.parent = b
c.leftChild = f
f.parent = c
c.rightChild = g
g.parent = c
h = Tree(a)
print(nextNode(h,d).name)