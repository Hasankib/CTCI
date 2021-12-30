def matchedParens(l:int) -> [str]:
    result =[]
    global runningString
    global rightParens
    global leftParens
    def createMatch():
        global rightParens
        global leftParens
        global runningString
        print(runningString,leftParens,rightParens,"*")
        if(rightParens == l):
            result.append(runningString[:])
            runningString = runningString[:len(runningString) - 1]
            rightParens-=1
            return
        if(leftParens < l):
            runningString += ("(")
            leftParens += 1
            createMatch()
        print(runningString,leftParens,rightParens,">")
        if(rightParens < l):
            rightParens += 1
            runningString += (")")
            createMatch()
        print(runningString,leftParens,rightParens,"!")
        if(leftParens > rightParens):
                leftParens -= 1
                runningString = runningString[:len(runningString) - 1]
        print(runningString,leftParens,rightParens,"?")
        return
    createMatch()
    return result
rightParens,leftParens,runningString = 0,0,""
print(matchedParens(2))