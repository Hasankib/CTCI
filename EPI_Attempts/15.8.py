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

def generateBinaryTrees(input:int) -> list[node]:
    def generate(numNodes:int,currentNodes: list[node]):
        if numNodes == input:
            result.append(currentNodes.copy())
            currentNodes.pop()
            numNodes -= 1
            return
        numNodes += 1
        currentNodes


    result = []