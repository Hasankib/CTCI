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

8.4