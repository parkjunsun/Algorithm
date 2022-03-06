n, k = map(int, input().split())
arr = list(map(int, input().split()))

right = 0
total = 0
for i in range(k):
    total += arr[i]
ans = total
cnt = 0

for left in range(1, n-(k-1)):
    total -= arr[left-1]
    total += arr[left+(k-1)]
    ans = max(ans, total)

print(ans)