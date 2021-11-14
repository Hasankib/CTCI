# # ##8.1
# # def tripStep(n):
# #     total = 0
# #     memo = [0 for i in range(n+1)]
# #     return tripStepHelper(1,n,total,memo) + tripStepHelper(2,n,total,memo) + tripStepHelper(3,n,total,memo) 

# # def tripStepHelper(m:int, n :int, total: int,memo:list):
# #     if(m == n):
# #         return 1
# #     for i in range(1,4):
# #         if(m+i <= n):
# #             if (memo[m+i] != 0):
# #                 total += memo[m+i]
# #             else:
# #                 total += tripStepHelper(m + i, n , total,memo)
# #     memo[m] = total
# #     return total
# # print(tripStep(24))

# ##8.2
# def robotInGrid(r:int,c:int,grid:list):
#     memo = [[True * c] * r]
#     path = []
#     robotGridHelp(0,0,r - 1,c - 1,grid,memo,path)

# def robotGridHelp(tempr:int,tempc:int,r:int,c:int,grid:list,memo:list,path:list):
#     tempPath = False
#     path.append(str(tempr)+str(tempc))
#     if(tempr == r and tempc == c):
#         return path
#     else:
#         if(tempc < c and memo[tempr][tempc + 1]):
#             path = robotGridHelp(tempr,tempc+1,r,c,grid,memo,path)
#             tempPath = path
#         if(tempr < r and tempPath == False and memo[tempr + 1][tempc]):
#             path = robotGridHelp(tempr+1,tempc,r,c,grid,memo,path)
#             tempPath = path
#         if(tempPath == False):
#             memo[tempr][tempc] = False
#             return False
#     return path

# 8.3
# def callerFunction(A:list):
#     midpt = (len(A)-1)//2
#     return magicIndex(A,midpt,0)

# def magicIndex(A:list,currentMidpt:int,ogMidpt:int):
#     print("A",A)
#     print("len A", len(A))
#     print("current,",currentMidpt, "og,",ogMidpt)
#     if(A[currentMidpt] == ogMidpt):
#         print("YEO")
#         return currentMidpt + 1
#     if(len(A) <= 1):
#         print(A,"WHAT?")
#         return False
#     else:
#        # if(currentMidpt != 0):
#         above = magicIndex(A[currentMidpt+1:],((currentMidpt + len(A))//2) - (currentMidpt+1),currentMidpt + ogMidpt)
#         print("YEO0",above)
#         if (above != False):
#             print("YEO1")
#             return above
#         print("AA",A)
#         below = magicIndex(A[:currentMidpt+1],(currentMidpt//2),currentMidpt)
#         print("YEO2",above)
#         if(below != False):
#             print("YEO13")
#             return below
#         else:
#             return False

# print(callerFunction([0,2,5,6,89,10,25,7,90]))


# a = [90]
# print(a[:0])

# 8.4

# def powerSet(setA:set):
#     if(len(setA) == 0):
#         return setA

#     elif(len(setA) == 1):
#         return setA, set()
#     else:
#         a = {}
#         x = set()
#         listA = []
#         return powerSetHelper(setA,a,[x])


# def powerSetHelper(setA:set,a:dict,lista:list):
#         if(setA == set()):
#             return lista
#         poppedElement = setA.pop()
#         tmpList = []
#         if(not(poppedElement in a)):
#             for i in lista:
#                 x = i.copy()
#                 x.add(poppedElement)
#                 tmpList.append(x)
#             a[poppedElement] = True
#         lista = lista + tmpList
#         return powerSetHelper(setA,a,lista)


# print(len(powerSet({1,2,3,4,5})))


# b = [1,2,3]
# c = list(b)
# b.extend(c)
# print(b)
# for i in range (len(b)//2,len(b)):
#     b[i] += 1

# print(b)

#8.5




# def cutTheRod(n,weights:[int]) -> int :
#     memo = [0 for i in range(len(weights))]
#     for i in range(len(weights)):
#         memo = cutTheRodHelp(i,weights,memo)
#     return memo[-1]

# def cutTheRodHelp(start,weights,memo):
#     for i in range(0,start//2):
#         if((memo[i] + memo[start-i - 1])>memo[start]):
#             memo[start] = memo[i] + memo[start-i - 1]
#     if(start//2 *2 == start):
#         if(memo[start//2]*2 > memo[start]):
#             memo[start] = memo[start//2]
#     if(weights[start]>memo[start]):
#         memo[start] = weights[start]
#     print(memo)
#     return memo

# print(cutTheRod(8,[1,5,8,9,10,17,17,20]))

# print(16.5%16)
#print(ord('a'))




# def smallestAlphabeticalManipulation(s):
#     if(len(s) == 0 or len(s) == 1):
#         return s
    
# 8.7
# def permsWithoutDups(string:str) -> list(str):
#     memoHash = {}
#     permHolder = []
#     length = len(string)
#     if(length == 0):
#         return None
#     elif(length == 1):
#         return string
#     else:
#         for i in range(len(string)):
#             permsWithoutDups(string[:i] + string[i:],memoHash,permHolder,[],string[i])

# def permsWithoutDupsHelper(string:str,memoHash:dict,permHolder:list(str),currentPerms:list,letter) -> list(str):
#     if(len(string) == 1):
#         currentPerms.append(string)
#         memoHash[string] = [string]
#         return currentPerms,memoHash
#     if(string in memoHash):
#         for i in currentPerms:
#             for x in memoHash[string]:
#                 i += x
#     for i in range(i,len(string)):

#         permsWithoutDupsHelper(string,memoHash)
        

##8.5

# def recursiveMultiply(inta:int,intb:int) -> int:
