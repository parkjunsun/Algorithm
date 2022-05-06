from collections import deque

m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                q.append((i, j, k, 0))
                visited[i][j][k] = 1


def bfs():
    while q:
        z, x, y, depth = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nz < h and -1 < nx < n and -1 < ny < m:
                if board[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    q.append((nz, nx, ny, depth + 1))
                    board[nz][nx][ny] = 1
                    visited[nz][nx][ny] = 1

    if check():
        return -1
    else:
        return depth


def check():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 0:
                    return True


print(bfs())
