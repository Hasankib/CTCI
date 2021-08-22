class node:
    def __init__(self,name:int):
        self.name = name
        self.leftChild = None
        self.rightChild = None
        self.next = None

class Tree:
    def __init__(self,root:node):
        self.root = root
    def printTree(self,root,text,parent):
        if(root == None):
            return
        print(root.name,text,parent)
        self.printTree(root.leftChild,"left Child of",root.name)
        self.printTree(root.rightChild,"right Child of",root.name)

def checkBalanced(tree:Tree):
    height = 0
    a = checkBalancedHelper(tree.root.leftChild,height)
    b = checkBalancedHelper(tree.root.rightChild,height)
    if(a != -1 and b != -1 and a == b):
        return True
    return False

def checkBalancedHelper(node:node,height):
    if(node == None):
        return height
    height += 1
    a = checkBalancedHelper(node.leftChild,height)
    b = checkBalancedHelper(node.rightChild,height)
    if (a != -1 and b != -1 and a == b):
        return height
    else:
        return -1

a = node(4)
b = node(2)
c = node(6)
d = node(1)
e = node(3)
f = node(5)
g = node(7)
a.leftChild = b
b.leftChild = d
a.rightChild = c
b.rightChild = e
c.leftChild = f
c.rightChild = g
g.leftChild = node(10)
h = Tree(a)
print(checkBalanced(h))