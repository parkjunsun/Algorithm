dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
