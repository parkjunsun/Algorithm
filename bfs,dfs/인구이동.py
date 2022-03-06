from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
sign = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(x, y, s):
    q = deque()
    q.append((x, y))
    visited2[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if l <= abs(board[x][y] - board[nx][ny]) <= r and visited2[nx][ny] == 0:
                    sign[x][y] = s
                    sign[nx][ny] = s
                    visited2[nx][ny] = 1
                    q.append((nx, ny))

def bfs(x, y, c):
    arr = [(x, y)]
    sums = board[x][y]
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if sign[nx][ny] == c and visited[nx][ny] == 0:
                    sums += board[nx][ny]
                    cnt += 1
                    visited[nx][ny] = 1
                    arr.append((nx, ny))
                    q.append((nx, ny))
    calc = sums // cnt
    for pos in arr:
        board[pos[0]][pos[1]] = calc

total = 0
s = 1

while True:
    flag = False
    save = deque()
    tmp = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if not visited2[i][j]:
                check(i, j, s)
                s += 1

    for i in range(n):
        for j in range(n):
            if sign[i][j] not in save and sign[i][j] != 0:
                save.append(sign[i][j])


    for i in range(n):
        for j in range(n):
             if sign[i][j] and visited[i][j] == 0:
                bfs(i, j, save.popleft())

    for i in range(n):
        for j in range(n):
            if tmp[i][j] != board[i][j]:
                flag = True
    if flag:
        total += 1
    else:
        break

    sign = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    visited2 = [[0] * n for _ in range(n)]

print(total)

