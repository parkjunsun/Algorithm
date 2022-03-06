n, m = map(int, input().split())
arr = list(map(int, input().split()))

right = 0
ans = 0
sum = 0

for left in range(n):
    while sum < m and right < n:
        sum += arr[right]
        right += 1
    if sum == m:
        ans += 1
    sum -= arr[left]

print(ans)

