class node:
    def __init__(self,name:int):
        self.name = name
        self.leftChild = None
        self.rightChild = None
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

def firstCommonAncestor(tree:Tree,node1:node,node2:node):
    tmp = node1
    node1List = []
    while(tmp.parent):
        if(tmp == tmp.parent.leftChild):
            node1List.append(1)
        else:
            node1List.append(0)
        tmp = tmp.parent

    tmp = node2
    node2List = []
    while(tmp.parent):
        if(tmp == tmp.parent.leftChild):
            node2List.append(1)
        else:
            node2List.append(0)
        tmp = tmp.parent

    if(node1List[-1] != node2List[-1]):
        return tree.root
    else:
        i = -1
        while( node1List[i] == node2List[i] and abs(i) <= len(node1List) and abs(i) <= len(node2List)):
            i -= 1
        i += 1

    tmp = tree.root

    for i in range(abs(i)):
        if(node1List[i] == 1):
            tmp = tmp.leftChild
        else:
            tmp = tmp.rightChild
    
    return tmp


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
print(firstCommonAncestor(h,e,f).name)