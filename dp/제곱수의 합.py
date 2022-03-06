n = int(input())
dp = [i for i in range(n+1)]

for i in range(2, n+1):
    for j in range(2, i):
        if j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)

print(dp[n])