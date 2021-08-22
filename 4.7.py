class node:
    def __init__(self,name:int):
        self.name = name
        self.parents = []
        self.numParents = 0
        self.noChildren = True
        self.marked = False

class Tree:
    def __init__(self,root:node):
        self.root = root
    def printTree(self,root,text,parent):
        if(root == None):
            return
        print(root.name,text,parent)
        self.printTree(root.leftChild,"left Child of",root.name)
        self.printTree(root.rightChild,"right Child of",root.name)

def buildOrder_helper(orderedList:list,noChildren:list,Index:int,node:node):
        if(node.numParents == 0):
            node.marked = True
            orderedList.append(node.name)
            if(Index == len(noChildren) - 1):
                return orderedList
            else:
                buildOrder_helper(orderedList,noChildren,Index+1,noChildren[Index + 1])
        else:
            for i in node.parents:
                if(not i.marked):
                    buildOrder_helper(orderedList,noChildren,Index,i)
                    i.marked = True
                node.numParents -= 1
            node.marked = True
            orderedList.append(node.name)
        return orderedList

def buildOrder(projects:list,dependencies:list):
    dictionaryNodes = {}
    noChildren = []
    for i in projects:
        a = node(i)
        dictionaryNodes[i] = a
    for i in dependencies:
        dictionaryNodes[i[1]].parents.append(dictionaryNodes[i[0]])
        dictionaryNodes[i[1]].numParents += 1
        dictionaryNodes[i[0]].noChildren = False
    for i in dictionaryNodes:
        if(dictionaryNodes[i].noChildren):
            noChildren.append(dictionaryNodes[i])
    orderedList = []
    orderedList = buildOrder_helper(orderedList,noChildren,0,noChildren[0])
    return orderedList

    
projects = ['a','b','c','d','e','f']
dependencies = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c']]
print(buildOrder(projects,dependencies))