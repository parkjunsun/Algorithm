n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    a, b, c = int(1e9), int(1e9), int(1e9)
    if i % 3 == 0:
        a = dp[i//3]
    if i % 2 == 0:
        b = dp[i//2]
    c = dp[i-1]

    dp[i] = min(a, b, c) + 1

print(dp[n])