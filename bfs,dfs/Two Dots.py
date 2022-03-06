import sys


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input())))

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, depth, alpha, fx, fy):
    if visited[x][y] == 1 and depth >= 4:
        return True

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx != fx or ny != fy:
            if -1 < nx < n and -1 < ny < m:
                if board[nx][ny] == alpha:
                    if dfs(nx, ny, depth+1, alpha, x, y):
                        return True
    return False


ans = False

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            if dfs(i, j, 0, board[i][j], i, j):
                ans = True
                break

if ans:
    print("Yes")
else:
    print("No")

