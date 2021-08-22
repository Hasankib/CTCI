class node:
    def __init__(self,name:int):
        self.name = name
        self.leftChild = None
        self.rightChild = None

class Tree:
    def __init__(self,root:node):
        self.root = root
    def printTree(self,root,text:str):
        if(root == None):
            return
        print(root.name,text)
        self.printTree(root.leftChild,"left")
        self.printTree(root.rightChild,"right")
        
def minTree(array:list):
    array2 = []
    for i in (array):
        array2.append(node(i))
    rootIndex = len(array2)//2
    tree = Tree(array2[rootIndex])
    if(len(array2) == 1):
        return tree
    minTreeHelper(array2[0:rootIndex],array2[rootIndex])
    minTreeHelper(array2[rootIndex + 1: len(array2)],array2[rootIndex])
    return tree

def minTreeHelper(array2:list,prevNode):
    if(len(array2) == 0):
         return
    elif(len(array2) == 1):
        if(array2[len(array2)//2].name<=prevNode.name):
            prevNode.leftChild = array2[0]
            return
        else:
            prevNode.rightChild = array2[0]
            return
    else:
        prevNodeIndex = len(array2)//2
        if(array2[prevNodeIndex].name<=prevNode.name):
            prevNode.leftChild = array2[prevNodeIndex]
        else:
            prevNode.rightChild = array2[prevNodeIndex]
        minTreeHelper(array2[0:prevNodeIndex],array2[prevNodeIndex])
        minTreeHelper(array2[prevNodeIndex + 1 : len(array2)],array2[prevNodeIndex])
        return


b = minTree([1,2,3,4])
print("-----")
b.printTree(b.root,"root")
c = minTree([1,2,3,4,5,6])
print("-----")
c.printTree(c.root,"root")
d = minTree([1,2,3,4,5,6,7])
print("-----")
d.printTree(d.root,"root")
d = minTree([1])
print("-----")
d.printTree(d.root,"root")
e = minTree([1,2,3])
print("-----")
e.printTree(e.root,"root")
f = minTree([1,2,2,3])
print("-----")
f.printTree(f.root,"root")