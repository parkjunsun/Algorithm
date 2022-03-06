n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        down = i + board[i][j]
        right = j + board[i][j]

        if down < n:
            dp[down][j] += dp[i][j]
        if right < n:
            dp[i][right] += dp[i][j]

print(dp[-1][-1])