n = int(input())
tmp = []
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    tmp.append((a, b))

tmp.sort(key=lambda x:x[0])
for t in tmp:
    arr.append(t[1])

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

m = max(dp)
print(n - m)