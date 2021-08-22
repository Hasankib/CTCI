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

class LinkedList:
    def __init__(self,head):
        self.head = head
        self.last = self.head
    
    def addToList(self,node:node):
        self.last.next = node
        self.last = node

    def printList(self):
        length = 1
        tmp = self.head
        print(tmp.name)
        while(tmp.next != None):
            tmp = tmp.next
            print(tmp.name)
            length += 1
        return length

def listOfDepths(tree:Tree):
    listOfLists = [LinkedList(tree.root)]
    count = 1
    listOfLists = listOfDepthsHelper(tree.root.leftChild,listOfLists,count)
    listOfLists = listOfDepthsHelper(tree.root.rightChild,listOfLists,count)
    return listOfLists

def listOfDepthsHelper(node:node,listOfLists:[],count:int):
    if(node == None):
        return listOfLists
    else:
        if(len(listOfLists)<count + 1):
            a = LinkedList(node)
            listOfLists.append(a)
        else:
            listOfLists[count].addToList(node)
        count = count + 1
        listOfLists = listOfDepthsHelper(node.leftChild,listOfLists,count)
        listOfLists = listOfDepthsHelper(node.rightChild,listOfLists,count)
    return listOfLists

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
h = Tree(a)
for i in listOfDepths(h):
    print("---")
    i.printList()
l = Tree(g)
for i in listOfDepths(l):
    print("---")
    i.printList()