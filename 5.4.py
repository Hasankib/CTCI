def nextNumber(posInt:int) -> int:
    holder = posInt
    numZeros = 0
    numOnes = 0
    firstZeroPos = 0
    secondZeroPos = 0
    firstOnepos = 0
    mask1 = 1
    i = 0
    if(mask1 & posInt == 1):
        return  - 1

    while(numZeros < 2):
        tmp = posInt & mask1
        posInt = posInt >> 1
        if(tmp == 1 and not numOnes):
            numOnes += 1
            firstOnepos = i
            numZeros += 1
            firstZeroPos = i - 1
        else:
            if(numZeros == 1 and numOnes == 1):
                secondZeroPos = i
                numZeros += 1
        i += 1
            

    nextSmallest = holder
    nextLargest = holder


    nextSmallest = nextSmallest | (1 << firstZeroPos)
    nextLargest = nextLargest | (1 << secondZeroPos + 1)

    mask = ~(1 << firstOnepos)

    nextSmallest = nextSmallest & mask
    nextLargest = nextLargest & mask

    return nextLargest,nextSmallest


print(nextNumber(6))