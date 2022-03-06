n, k = map(int, input().split())
coins = []

for _ in range(n):
    coin = int(input())
    coins.append(coin)

total = 0

for i in range(n-1, -1, -1):
    if k == 0:
        break
    if coins[i] > k:
        continue
    total += k // coins[i]
    k %= coins[i]

print(total)
