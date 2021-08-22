#Zero Matrix
a = [[1,0,3,4],[5,6,7,8],[9,10,0,12],[13,14,15,16]]
hashmap = {}
N = 4
class matrix_position:
    def __init__ (self,i,j):
        self.i = i
        self.j = j
for i in range(N):
    for j in range (N):
        if (a[i][j] == 0):
            intial_position = matrix_position(i,j)
            hashmap[intial_position] = True
for i in hashmap:
    for p in range(N):
        if(p == i.i):
            for b in range (N):
                    a[p][b] = 0
    for p in range(N):
        for b in range (N):
            if(b == i.j):
                    a[p][b] = 0
for i in range(N):
    for j in range (N):
        print(a[i][j])