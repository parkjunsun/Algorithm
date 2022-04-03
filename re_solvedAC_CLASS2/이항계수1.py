n, k = map(int, input().split())

up, down = 1, 1

for i in range(n, n-k, -1):
    up *= i

for i in range(k, 0, -1):
    down *= i

print(up // down)