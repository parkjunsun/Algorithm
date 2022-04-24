import sys

n = int(input())

steps = [0] * (n + 1)

for i in range(1, n + 1):
    a = int(input())
    steps[i] = a

if n == 1:
    print(steps[1])
    sys.exit()

dp = [0] * (n + 1)
dp[1] = steps[1]
dp[2] = dp[1] + steps[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 2] + steps[i], dp[i - 3] + steps[i - 1] + steps[i])

print(dp[-1])
