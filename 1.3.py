string1 = "a b c d e f   "
x = 11
def checker(string,truelen):
    hashmap = {}
    for i in range(truelen):
        if (string[i] == ' '):
            hashmap[i] = "%20"
        else:
            hashmap[i] = string[i]
    string = ""
    for i in range(truelen):
        string+=hashmap[i]
    return string
print(checker(string1,11))
