from collections import deque
import sys

m, n, h = map(int, input().split())

board = []

for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    board.append(tmp)

check = 0
already = False
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 0:
                check += 1

if not check:
    print(0)
    sys.exit()

dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

visited = [[[0] * m for _ in range(n)] for _ in range(h)]
q = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 1:
                q.append((k, i, j, 0))
                visited[k][i][j] = 1


while q:
    z, x, y, depth = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nz < h and -1 < nx < n and -1 < ny < m:
            if board[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                board[nz][nx][ny] = 1
                visited[nz][nx][ny] = 1
                q.append((nz, nx, ny, depth + 1))

check = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if board[k][i][j] == 0:
                check += 1

if check:
    print(-1)
else:
    print(depth)




