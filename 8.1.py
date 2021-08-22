##8.1
def tripStep(n):
    total = 0
    memo = [0 for i in range(n+1)]
    return tripStepHelper(1,n,total,memo) + tripStepHelper(2,n,total,memo) + tripStepHelper(3,n,total,memo) 

def tripStepHelper(m:int, n :int, total: int,memo:list):
    if(m == n):
        return 1
    for i in range(1,4):
        if(m+i <= n):
            if (memo[m+i] != 0):
                total += memo[m+i]
            else:
                total += tripStepHelper(m + i, n , total,memo)
    memo[m] = total
    return total
print(tripStep(24))

##8.2
# def robotInGrid(r:int,c:int,grid:list):
#     memo = [[True for i in range c] for x in range r]
#     robotGridHelp(r,c,grid,memo)

# def robotGridHelp(r:int,c:int,grid:list,memo:list):
#     if(grid[r+1][c] == False and grid[r][c+1]==False and grid[r+1][c+1]==False):
#         memo.pop()
#         return
    
#     while(grid[r][c]!=False):
#         memo.append([r,c])
#         if(grid[r+1][c+1] == True):
#             robotGridHelp(r+1,c+1,grid,memo)
#         elif(grid[r+1][c] == True):
#             robotGridHelp(r+1,c,grid,memo)
#         elif(grid[r][c+1] == True):
#             robotGridHelp(r+1,c,grid,memo)

