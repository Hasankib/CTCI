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
        return "Empty"
    def isEmpty(self):
        return self.top == None 


class MyQueue:
    def __init__(self):
        self.newStack = Stack()
        self.oldStack = Stack()
    
    def push(self,data):
        self.newStack.push(data)
    
    def shiftBetweenStacks(self):
        if(self.oldStack.isEmpty()):
            while(not self.newStack.isEmpty()):
                self.oldStack.push(self.newStack.pop().data)

    def dequeue(self):
        self.shiftBetweenStacks()
        print(self.oldStack.pop().data)

a = MyQueue()
a.push(5)
a.push(3)
a.dequeue()