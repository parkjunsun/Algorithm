import math

n, m = map(int, input().split())

tmp = [True for i in range(m+1)]
tmp[0], tmp[1] = False, False

for i in range(2, int(math.sqrt(m))+1):
    if tmp[i]:
        x = 2
        while i * x <= m:
            tmp[i*x] = False
            x += 1

for i in range(n, m+1):
    if tmp[i]:
        print(i)