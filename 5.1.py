# num = 8
# print(num | (1<<2))
# print((1<<0))
# print(num)

M = 19
N = 1024
i = 2
j = 6
M = 19
mask = ~0
print(mask)
leftmask = mask << (j + 1)
print(leftmask)
rightmask = (1 << i) - 1
print(rightmask)
mask = rightmask | leftmask
N = N & mask
M = M << i
N = N | M
print(N)
