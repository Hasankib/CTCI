class node:
    def __init__(self,name:str,adjList:list):
        self.name = name
        self.children = adjList
        self.front = None
        self.behind = None

class Graph:
    def __init__(self,nodes:list):
        self.nodes = nodes
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

def routeBetween(graph:Graph,node1:node,node2:node):
    marked= {}
    queue = Queue()
    for i in graph.nodes:
        marked[i] = False

    marked[node1] = True
    queue.enqueue(node1)


    while(not queue.isEmpty()):
        r = queue.dequeue()
        marked[r] = True

        for i in r.children:
            if(marked[i] == False):
                marked[i] = True
                if(i == node2):
                    return True
                queue.enqueue(i)
    
    for i in marked:
        marked[i] = False

    marked[node2] = True
    queue.enqueue(node2)

    while(not queue.isEmpty()):
        r = queue.dequeue()
        marked[r] = True

        for i in r.children:
            if(marked[i] == False):
                marked[i] = True
                if(i == node1):
                    print('ye')
                    return True
                queue.enqueue(i)
    
    return False

b = node('b',[])
c = node('c',[b])
a = node('a',[b,c])
d = node('d',[])
graph = Graph([a,b,c])
e = routeBetween(graph,d,a)
print(e)