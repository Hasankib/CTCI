def PathswithSum(tree:Tree,sum:int):
    pathSumList = [tree.root.data]
    count = 0
    runningSum = tree.root.data
    dict = {}
    dict[tree.root.data] = 1
    count += pathswithSum_help(count,sum,dict,runningSum,tree.root.leftChild)
    count += pathswithSum_help(count,sum,dict,runningSum,tree.root.rightChild)
    return count

def pathswithSum_help(count: int,sum :int,dict:{},runningSum,pathSumList :[],node:node):
    if(node == None):
        return count
    runningSum += node.data
    a = runningSum - sum
    if(dict.get(a)):
        count += dict.get(a)
    if(dict.get(runningSum)):
        dict[runningSum] += 1
    else:
        dict[runningSum] = 1
    pathswithSum_help(count,sum,dict,runningSum,node.leftChild)
    pathswithSum_help(count,sum,dict,runningSum,node.rightChild)