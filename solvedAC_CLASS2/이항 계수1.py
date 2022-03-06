import sys

n, k = map(int, input().split())
if k == 0:
    print(1)
    sys.exit()

up = n
down = 1

for i in range(1, k):
    up *= n - i

for i in range(1, k):
    down *= i+1

print(up // down)