t = int(input())

dp1 = [0] * (40 + 1)
dp2 = [0] * (40 + 1)

dp1[0], dp2[0] = 1, 0
dp1[1], dp2[1] = 0, 1

for i in range(2, 40 + 1):
    dp1[i] = dp1[i - 2] + dp1[i - 1]
    dp2[i] = dp2[i - 2] + dp2[i - 1]

for _ in range(t):
    n = int(input())
    print(dp1[n], dp2[n])

