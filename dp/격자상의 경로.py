n, m, k = map(int, input().split())
board = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append((i*m)+(j+1))
    board.append(tmp)

x, y = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == k:
            x, y = i, j

dp = [[0] * (m+1) for _ in range(n+1)]
dp[1][1] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

before = dp[x+1][y+1]

dp = [[0] * (m+1) for _ in range(n+1)]
dp[x+1][y+1] = 1

for i in range(x+1, n+1):
    for j in range(y+1, m+1):
        if i == x+1 and j == y+1:
            continue
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

after = dp[n][m]
answer = before * after

print(answer)
