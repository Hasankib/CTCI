class node:
    def __init__(self,name:int):
        self.name = name
        self.leftChild = None
        self.rightChild = None

class Tree:
    def __init__(self,root:node):
        self.root = root
    def printTree(self,root,text,parent):
        if(root == None):
            return
        print(root.name,text,parent)
        self.printTree(root.leftChild,"left Child of",root.name)
        self.printTree(root.rightChild,"right Child of",root.name)

def BSTsequences(tree:Tree):
    doubleCount = 0
    childrenList = [tree.root.name]
    childrenList,doubleCount = helper(tree.root,doubleCount,childrenList)
    print(childrenList,doubleCount)
    allArrays = [[] for i in range (2**doubleCount)]
    


def helper(node:node,doubleCount:int,childrenList:list):
    if(node.leftChild and node.rightChild):
        doubleCount += 1
        childrenList.append(node.leftChild.name)
        childrenList.append(node.rightChild.name)
    elif(node.leftChild or node.rightChild):
        if(node.leftChild):
            childrenList.append(node.leftChild.name)
            childrenList,doubleCount = helper(node.leftChild,doubleCount,childrenList)
            return childrenList,doubleCount
        else:
            childrenList.append(node.rightChild.name)
            childrenList,doubleCount = helper(node.rightChild,doubleCount,childrenList)
            return childrenList,doubleCount
    else:
        return childrenList,doubleCount
    childrenList,doubleCount = helper(node.leftChild,doubleCount,childrenList)
    childrenList,doubleCount = helper(node.rightChild,doubleCount,childrenList)
    return childrenList,doubleCount

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
BSTsequences(h)