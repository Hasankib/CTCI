girl = 50
a = 25
boy = 0
currentBoys = 1
while(a <= 50):
    boy += (currentBoys) * (a)
    currentBoys += 1
    girl += 1
    a += a/2
print(girl/boy)