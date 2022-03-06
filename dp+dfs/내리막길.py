n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dp = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if board[nx][ny] < board[x][y]:
                    for r in range(n):
                        for c in range(m):
                            print(dp[r][c], end='  ')
                        print()
                    print()
                    dp[x][y] += dfs(nx, ny)
    for i in range(n):
        for j in range(m):
            print(dp[i][j], end='  ')
        print()
    print()
    return dp[x][y]


print(dfs(0, 0))
