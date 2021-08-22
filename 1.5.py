string1 = "pale"
string2 = "ple"
def checker(stringa,stringb):
    if(stringa == stringb):
        return True

    if(len(stringb)>len(stringa)):
        temp = stringa
        stringa = stringb 
        stringb = temp

    if((len(stringa)-len(stringb))>1):
        return False

    if(len(stringa) == len(stringb)):
        if((helper(stringa,stringb))>1):
            return False
        else:
            return True

    if(helper2(stringa,stringb)>0):
        return False
    return True

def helper(string1,string2):
    diffcounter = 0
    for i in range( len(string2)):
        if(string1[i]!=string2[i]):
            diffcounter+=1
    return diffcounter

def helper2(string1,string2):
    differcounter = 0
    for i in range(len(string1)):
        if(string1[i]!=string2[i]):
            string1 = string1[:i] + string1[(i+1):]
    for i in range(len(string1)):
        if(string1[i]!=string2[i]):
            differcounter+=1
    return differcounter
