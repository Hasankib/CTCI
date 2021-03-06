class queueNode:
    def __init__ (self,data,front,behind):
        self.data = data
        self.front = front
        self.behind = behind

class LinkedList:
    def __init__ (self,list1):
        self.head = None
        self.tail = None
        for i in range(len(list1)-1, -1, -1):
            if(i==len(list1) - 1):
                x = queueNode(list1[i],None,None)
                self.tail = x
                y = x
            else:
                x = queueNode(list1[i],y,None)
                y = x
            if(i == 0):
                self.head = y
            

    def getlength(self):
        length = 1
        n = self.head
        while(n.front!=None):
            n = n.front   
            length+=1
        return length

    def dequeueList(self):
        n = self.head
        while(n.front!=self.tail):
            n = n.front
        n.front = None
        self.tail = n
    
    def enqueueList(self,node):
        if(not self.tail):
            self.tail = node
        node.front = self.head
        self.head = node

class Queue:
    def __init__(self):
        self.first = None
        self.last = self.first
    def add(self,node):
        if(self.first == None):
            self.first = node
            self.last = self.first
        else:
            if(self.first == self.last):
                self.last = node
                self.last.front = self.first
                self.first.behind = self.last
            else:
                tmp = self.last
                self.last = node
                self.last.front = tmp
                self.last.front.behind = self.last
    def remove(self):
        if(self.first==None):
            print("error")
        elif(self.first == self.last):
            self.first = None
            self.last = None 
        else:
            self.first = self.first.behind
            self.first.front = None
    def peek(self):
        return self.first
    def isEmpty(self):
        return self.last == None and self.first == None

class animalShelter:
    def __init__(self):
        self.ll = LinkedList([])
        self.catQueue = Queue()
        self.dogQueue = Queue()
        self.oldestCat = None
        self.oldestDog = None
    def enqueue(self,animalType):
    ## 0 means cat and 1 means dog
        if(animalType == 0):
            cat = queueNode(animalType,None,None)
            self.catQueue.add(cat)
            self.ll.enqueueList(cat)
        if(animalType == 1):
            dog = queueNode(animalType,None,None)
            self.dogQueue.add(dog)
            self.ll.enqueueList(dog)
    def dequeueAny(self):
        if(self.ll.tail.data == 0):
            self.catQueue.remove()
        elif(self.ll.tail.data == 1):
            self.dogQueue.remove()
        self.ll.dequeueList()
    def dequeueDog(self):
        node = self.dogQueue.peek()
        self.dogQueue.remove()
        if(self.ll.tail == node):
            self.ll.tail.dequeueList()
        else:
            tmp = self.ll.head
            while(tmp.front != node):
                tmp = tmp.next
            tmp.front = node.front
    def dequeueCat(self):
        node = self.catQueue.peek()
        self.catQueue.remove()
        if(self.ll.tail == node):
            self.ll.tail.dequeueList()
        else:
            tmp = self.ll.head
            while(tmp.front != node):
                tmp = tmp.next
            tmp.front = node.front
    def printList(self):
        tmp = self.ll.head
        print(tmp.data)
        while(tmp.front!=None):
            tmp = tmp.front
            print(tmp.data)

a = animalShelter()
a.enqueue(0)
a.enqueue(1)
a.enqueue(0)
a.enqueue(1)
a.enqueue(0)
a.enqueue(0)
a.enqueue(1)
a.enqueue(1)
a.enqueue(1)
print(a.ll.getlength())
a.printList()
print("----")
a.dequeueAny()
print("----")
print(a.ll.getlength())
a.printList()
