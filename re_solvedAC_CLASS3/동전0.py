n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
ans = 0


for coin in arr:
    if k == 0:
        break
    if coin > k:
        continue
    ans += k // coin
    k %= coin

print(ans)