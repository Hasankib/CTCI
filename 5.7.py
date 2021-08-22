y = 0xaaaaaaaa
x = 0x55555555
c= 2 + 4 + 32 + 64 + 256 + 4096
print("c", c)
evenDigits = c & y
evenDigits = evenDigits << 1
print(evenDigits)
oddDigits = c & x
print("oddDigits" ,oddDigits)
oddDigits = oddDigits >> 1
print("oddDigitss" ,oddDigits)
print(oddDigits)
c = evenDigits | oddDigits

print("c",c)
print(8 + 128 + 512 + (4096)*2)