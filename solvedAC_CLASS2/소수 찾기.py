import math

n = int(input())
arr = list(map(int, input().split()))
last = max(arr)

sosu = [True] * (last + 1)
sosu[0] = False
sosu[1] = False

for i in range(2, int(math.sqrt(last)) + 1):
    if sosu[i]:
        x = 2
        while i * x <= last:
            sosu[i * x] = False
            x += 1

answer = 0
for num in arr:
    if sosu[num]:
        answer += 1

print(answer)