import math
n, m = map(int, input().split())

chk = [True] * (m+1)
chk[0] = False
chk[1] = False

for i in range(2, int(math.sqrt(m))+1):
    if chk[i]:
        x = 2
        while i * x <= m:
            chk[i*x] = False
            x += 1

for i in range(n, m+1):
    if chk[i]:
        print(i)


