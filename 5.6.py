def Conversion(a:int,b:int) -> int:
    track = 0
    c = a ^ b
    while(c!=0):
        if(c != 0):
            track += 1
        c = c & (c - 1)

    return track

print(Conversion(29,15))