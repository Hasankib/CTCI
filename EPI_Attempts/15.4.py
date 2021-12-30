import math

def powerSet(s:set)->set:
    def powerSetter(i):
        if(i == len(s) - 1):
            currentSet.append(s[i])
            result.append(currentSet.copy())
            currentSet.pop()
            return
        for j in range(i,len(s)):
            currentSet.append(s[j])
            result.append(currentSet.copy())
            powerSetter(j + 1)
            currentSet.pop()

    currentSet = []
    result = [[]]
    powerSetter(0)
    return result

print(powerSet([0]))