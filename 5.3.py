def FBtW(integer: int):
    currentZeros = 0
    longestStreak = 0
    currentStreak = 0
    while(integer != 0):
        tmp = integer & 1
        integer = integer >> 1
        if(tmp == 1):
            currentStreak += 1
        else:
            currentZeros += 1
            if(currentZeros == 2):
                if(currentStreak > longestStreak):
                    longestStreak = currentStreak
                currentStreak = 0
            currentStreak += 1
    return longestStreak

print(FBtW(1775))