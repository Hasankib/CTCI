def kSubSets(k:int,n:int):
    def generate(i):
        if(len(runningSet) == k):
            result.append(runningSet.copy())
        for j in range(i+1,n+1):
            if(len(runningSet) > 0):
                if(j>runningSet[-1]):
                    runningSet.append(j)
                    generate(i+1)
                    runningSet.pop()
            else:
                runningSet.append(j)
                generate(i+1)
                runningSet.pop()

    result = []
    runningSet = []
    generate(0)
    return result

print(kSubSets(3,5))