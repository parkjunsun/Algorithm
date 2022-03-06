from collections import deque
import sys

n, m, g = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
start_x, start_y = map(int, input().split())

pos = []
for _ in range(m):
    sx, sy, dx, dy = map(int, input().split())
    board[sx-1][sy-1] = 2
    pos.append((sx-1, sy-1, dx-1, dy-1))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_passenger(x, y, depth, gas):
    candidates = []
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((x, y, depth))
    visited[x][y] = 1
    while q:
        x, y, depth = q.popleft()
        if board[x][y] == 2:
            candidates.append((x, y, depth))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, depth + 1))
    candidates.sort(key=lambda x:(x[2], x[0], x[1]))
    if len(candidates) == 0:
        return -1, -1, -1
    remain = gas - candidates[0][2]
    board[candidates[0][0]][candidates[0][1]] = 0
    return candidates[0][0], candidates[0][1], remain


def find_goal(x, y, gas, goalx, goaly):
    depth = 0
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((x, y, depth))
    visited[x][y] = 1
    while q:
        x, y, depth = q.popleft()
        if x == goalx and y == goaly:
            return x, y, gas - depth, depth
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, depth+1))
    return -1, -1, -1, -1

flag = False
fx, fy, fg = find_passenger(start_x-1, start_y-1, 0, g)
if fg <= 0:
    print(-1)
    sys.exit()
gx, gy = 0, 0
for p in pos:
    if fx == p[0] and fy == p[1]:
        gx, gy = p[2], p[3]

rx, ry, gg, dist = find_goal(fx, fy, fg, gx, gy)
if gg < 0:
    print(-1)
    sys.exit()
else:
    rg = gg + dist*2

for _ in range(m-1):
    fx, fy, fg = find_passenger(rx, ry, 0, rg)
    if fg <= 0:
        flag = True
        break
    gx, gy = 0, 0
    for p in pos:
        if fx == p[0] and fy == p[1]:
            gx, gy = p[2], p[3]
    rx, ry, gg, dist = find_goal(fx, fy, fg, gx, gy)
    if gg < 0:
        flag = True
        break
    else:
        rg = gg + dist*2

if flag:
    print(-1)
else:
    print(rg)
