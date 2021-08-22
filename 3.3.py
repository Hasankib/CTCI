
class stackNode:
    def __init__ (self,data,next):
        self.data = data
        self.next = next

class SetofStacksNode:
    def __init__(self,nextStack):
        self.top = None
        self.nextStack = nextStack
        self.stackHeight = 0

class SetofStacks:
    def __init__(self,threshhold):
        self.threshhold = threshhold
        self.topStack = None
    def push(self,data):
        if(self.topStack == None):
            self.topStack = SetofStacksNode(None)
            self.topStack.top = stackNode(data,None)
            self.topStack.stackHeight += 1
        else:
            if(self.topStack.stackHeight<self.threshhold):
                self.topStack.top = stackNode(data,self.topStack.top)
                self.topStack.stackHeight += 1
                print(self.topStack.stackHeight)
            else:
                self.topStack = SetofStacksNode(self.topStack)
                self.topStack.top = stackNode(data,None)
                self.topStack.stackHeight += 1
                print(self.topStack.stackHeight)
    def pop(self):
        if(not self.topStack):
            return "Empty Stack Set"
        elif(self.topStack.stackHeight == 1):
            tmp = self.topStack.top.data
            self.topStack = self.topStack.nextStack
            return tmp
        else:
            tmp = self.topStack.top.data
            self.topStack.top = self.topStack.top.next
            self.topStack.stackHeight -= 1
            return tmp
    def popAt(self,index):
        tmp = self.topStack
        i = 0
        while(tmp!=None and i!=index):
            tmp = tmp.nextStack
            i+=1
        if(tmp):
            tmp2 = self.topStack
            self.topStack = tmp
            print(self.pop())
            self.topStack = tmp2

a = SetofStacks(4)
a.push(1)
a.push(2)
a.push(3)
print(a.pop())
a.push(1)
a.push(2)
a.push(3)
a.popAt(1)