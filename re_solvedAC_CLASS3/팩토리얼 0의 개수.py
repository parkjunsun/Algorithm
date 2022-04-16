import math

n = int(input())
fac = str(math.factorial(n))
rev = fac[::-1]

cnt = 0
for num in rev:
    if num != '0':
        break
    cnt += 1

print(cnt)