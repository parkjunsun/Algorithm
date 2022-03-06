from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

sx, sy, sd = map(int, input().split())
fx, fy, fd = map(int, input().split())

if sd == 1:
    sd = 1
elif sd == 2:
    sd = 3
elif sd == 3:
    sd = 2
else:
    sd = 0

if fd == 1:
    fd = 1
elif fd == 2:
    fd = 3
elif fd == 3:
    fd = 2
else:
    fd = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

def turn_right(direction):
    direction += 1
    if direction == 4:
        direction = 0
    return direction

def bfs(x, y, d, cnt):
    q = deque()
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]
    q.append((x, y, d, cnt))
    visited[x][y][d] = 1
    while q:
        x, y, direction, count = q.popleft()
        if fx-1 == x and fy-1 == y and direction == fd:
            return count

        nx = x + dx[direction]
        ny = y + dy[direction]
        if -1 < nx < n and -1 < ny < m:
            if board[nx][ny] == 0 and visited[nx][ny][direction] == 0:
                visited[nx][ny][direction] = 1
                q.append((nx, ny, direction, count+1))

        nx = x + dx[direction] * 2
        ny = y + dy[direction] * 2
        if -1 < nx < n and -1 < ny < m:
            if board[nx][ny] == 0 and board[nx-dx[direction]][ny-dy[direction]] == 0 and visited[nx][ny][direction] == 0:
                visited[nx][ny][direction] = 1
                q.append((nx, ny, direction, count+1))

        nx = x + dx[direction] * 3
        ny = y + dy[direction] * 3
        if -1 < nx < n and -1 < ny < m:
            if board[nx][ny] == 0 and board[nx-dx[direction]][ny-dy[direction]] == 0 and board[nx - dx[direction] * 2][ny - dy[direction] * 2] == 0 and visited[nx][ny][direction] == 0:
                visited[nx][ny][direction] = 1
                q.append((nx, ny, direction, count+1))


        ld = turn_left(direction)
        if visited[x][y][ld] == 0:
            visited[x][y][ld] = 1
            q.append((x, y, ld, count+1))

        rd = turn_right(direction)
        if visited[x][y][rd] == 0:
            visited[x][y][rd] = 1
            q.append((x, y, rd, count+1))

print(bfs(sx-1, sy-1, sd, 0))
