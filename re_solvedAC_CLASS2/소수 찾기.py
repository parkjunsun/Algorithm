import math

n = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)

sosu = [True for i in range(max_num + 1)]
sosu[0] = False
sosu[1] = False

for i in range(2, int(math.sqrt(max_num)) + 1):
    if sosu[i]:
        x = 2
        while i * x <= max_num:
            sosu[i * x] = False
            x += 1

cnt = 0
for num in arr:
    if sosu[num]:
        cnt += 1

print(cnt)
