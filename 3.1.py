from three import *

class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    def Push(self,item,stackNum):
        self.array[stackNum * self.size[stackNum]] = item
        self.size[stackNum] += 1