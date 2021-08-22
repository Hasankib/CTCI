class stackNode:
    def __init__ (self,data,next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    def pop(self):
        tmp = self.top
        self.top = self.top.next
        return tmp
    def push(self,data):
        self.top = stackNode(data,self.top)
    def peek(self):
        if(self.top):
            return self.top.data
        print("Empty")
        return None
    def isEmpty(self):
        return self.top == None 

class stackSorter:
    def __init__(self, sortableStack):
        self.sortableStack = sortableStack
        self.tmpStack = Stack()
        self.tmpStack.push(self.sortableStack.pop().data)
        while(not self.sortableStack.isEmpty()):
            if(self.sortableStack.peek()>=self.tmpStack.peek()):
                self.tmpStack.push(self.sortableStack.pop().data)
            else:
                tmpNode = self.sortableStack.pop()
                while(not self.tmpStack.isEmpty() and not self.tmpStack.peek()<=tmpNode.data):
                    self.sortableStack.push(self.tmpStack.pop().data)
                self.tmpStack.push(tmpNode.data)
        while(not self.tmpStack.isEmpty()):
            self.sortableStack.push(self.tmpStack.pop().data)
    
    def printStack(self):
        while(not self.sortableStack.isEmpty()):
            print(self.sortableStack.pop().data)

a = Stack()
a.push(1)
a.push(4)
a.push(3)
a.push(8)
a.push(-7)
a.push(0)
b = stackSorter(a)
b.printStack()