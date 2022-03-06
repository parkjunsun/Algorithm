import sys

n = int(input())
if n == 0:
    print(0)
    sys.exit()
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])