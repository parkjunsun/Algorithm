from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input())))

visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny] == color and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


cnt = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            cnt += 1
        if board[i][j] == 'G' and visited[i][j] == 0:
            bfs(i, j, 'G')
            cnt += 1
        if board[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            cnt += 1

visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R' and visited[i][j] == 0:
            bfs(i, j, 'R')
            cnt2 += 1
        if board[i][j] == 'B' and visited[i][j] == 0:
            bfs(i, j, 'B')
            cnt2 += 1

print(cnt, cnt2)

