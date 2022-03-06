import sys

n = int(input())
stairs = []
for _ in range(n):
    stair = int(input())
    stairs.append(stair)

dp = [0] * n
if n == 1:
    print(stairs[0])
    sys.exit()
dp[0] = stairs[0]
if n == 2:
    print(dp[0] + stairs[1])
    sys.exit()
dp[1] = dp[0] + stairs[1]
dp[2] = max(dp[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])


print(dp[-1])