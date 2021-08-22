string1 = "tact coobca"
def checker(string):
    hashmap = {}
    oddletters = 0
    for i in string:
        hashmap[i] = 0
    for i in string:
        hashmap[i]+=1
    for i in string:
        if (hashmap[i]%2==1 and i!=' '):
            oddletters+=1
    if oddletters>1:
        return False
    return True
if(checker(string1)):
    print("pailindrome")
