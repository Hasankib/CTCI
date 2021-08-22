class stackNode:
    def __init__ (self,data,next,next_highest):
        self.data = data
        self.next = next
        self.next_highest = next_highest

class Stack:
    def __init__(self):
        self.top = None
        self.min = None
    def pop(self):
        if(self.min == self.top):
            self.min = self.top.next_highest
        self.top = self.top.next
    def push(self,data):
        self.top = stackNode(data,self.top,None)
        if(self.top):
            if(not self.min):
                self.min = self.top
            else:
                if(self.min.data>self.top.data):
                    self.top.next_highest = self.min
                    self.min = self.top
    def peek(self):
        if(self.top):
            return self.top.data
        else:
            return "Empty Right Now"
    def get_min(self):
        if(self.min):
            return self.min.data
        else:
            return "Empty Right Now"
    def isEmpty(self):
        return self.top == None 

b = Stack()
print(b.peek())
print(b.get_min())
b.push(5)
b.push(3)
b.push(2)
b.push(8)
print(b.peek())
print(b.get_min())
b.pop()
print(b.get_min())
b.pop()
print(b.get_min())
b.pop()
print(b.peek())
print(b.get_min())
b.pop()
print(b.peek())
print(b.get_min())
#print(Stack.peek(self))
#a.push(1)
#a.push(2)

