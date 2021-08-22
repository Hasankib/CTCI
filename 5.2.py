def binaryToString(num:float) -> str:
    if(num <= 0 or num >= 1):
        return "ERROR"
    representation = "."
    while(num > 0):
        if(len(representation) == 32):
            return "ERROR"
        num *= 2
        if(num>=1):
            num -= 1
            representation += '1'
        else:
            representation += '0'
        
    return representation

print(binaryToString(0.25))
