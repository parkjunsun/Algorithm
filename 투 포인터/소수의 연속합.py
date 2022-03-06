import math

n = int(input())
arr = []

tmp = [True for i in range(n+1)]
for i in range(2, int(math.sqrt(n)) + 1):
    if tmp[i]:
        x = 2
        while i * x <= n:
            tmp[i*x] = False
            x += 1
for i in range(2, len(tmp)):
    if tmp[i]:
        arr.append(i)

right = 0
sums = 0
ans = 0

for left in range(len(arr)):
    while sums < n and right < len(arr):
        sums += arr[right]
        right += 1
    if sums == n:
        ans += 1
    sums -= arr[left]

print(ans)