#matrix rotation
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
N = 4
hashmap = {}
class matrix_position:
    def __init__ (self,i,j):
        self.i = i
        self.j = j
for i in range(N):
    for j in range(N):
        initial_positions = matrix_position(i,j)
        hashmap[initial_positions] = a[i][j]
for i in hashmap:
    a[i.j][N-1-(i.i)] = hashmap[i]
for i in range(N):
    for j in range(N):
        print(a[i][j])