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

def validateBST(tree:Tree):
    return validateBST_Help(tree.root)

def validateBST_Help(node:node):
    if(node == None):
        return True
    if((node.leftChild and node.leftChild.name>node.name) or (node.rightChild and node.rightChild.name<=node.name)):
        return False
    return validateBST_Help(node.leftChild) and validateBST_Help(node.rightChild)

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
#g.leftChild = node(10)
h = Tree(a)
print(validateBST(h))