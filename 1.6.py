#String Compression
from collections import OrderedDict
string = "aabcccccaaa"
x = 0
class letter:
    def __init__ (self,name,index):
        self.name = name
        self.index = index

hashmap = OrderedDict({})

while x<len(string)-1:
    temp = x
    compy = letter(string[temp],temp)
    hashmap[compy] = 1
    x+=1
    while(string[x]==string[x-1]):
        if(x == len(string)-1):
            hashmap[compy]+=1
            break
        else:
            x+=1
            hashmap[compy]+=1

string = ""

for i in hashmap:
    string+=i.name
    string+=str(hashmap[i])

print(string)