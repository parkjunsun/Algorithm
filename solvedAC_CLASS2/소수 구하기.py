import math

n, m = map(int, input().split())

sosu = [True for _ in range(m+1)]
sosu[0], sosu[1] = False, False

for i in range(2, int(math.sqrt(m))+1):
    if sosu[i]:
        x = 2
        while i * x <= m:
            sosu[i*x] = False
            x += 1

for i in range(n, m+1):
    if sosu[i]:
        print(i)

