from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

copied = deepcopy(board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, board):
    zeros = 0
    pos = []
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((x, y))
    visited[x][y] = 1
    init_num = board[x][y]
    while q:
        x, y = q.popleft()
        pos.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if (board[nx][ny] == init_num or board[nx][ny] == 0) and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    pos.sort(key=lambda x:(x[0], x[1]))
    for p in pos:
        if board[p[0]][p[1]] == 0:
            zeros += 1
    for p in pos:
        if board[p[0]][p[1]] != 0:
            standard = (p[0], p[1])
            break

    return len(pos), zeros, standard[0], standard[1], pos


def rotate_90(board):
    x = len(board)
    y = len(board[0])
    res = [[0] * y for _ in range(x)]

    for r in range(x):
        for c in range(y):
            res[c][x-r-1] = board[r][c]

    return res

def gravity(board):
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if board[j][i] != -2 and board[j][i] != -1:
                my_num = board[j][i]
                board[j][i] = -2
                while True:
                    nx = j + 1
                    ny = i
                    if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                        nx -= 1
                        break
                    if board[nx][ny] != -2:
                        nx -= 1
                        break
                    j, i = nx, ny
                board[nx][ny] = my_num
    return board

score = 0
while True:
    candidates = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and board[i][j] != -1 and board[i][j] != -2:
                board = deepcopy(copied)
                size, rainbow, st1, st2, p = bfs(i, j, board)
                candidates.append((size, rainbow, st1, st2, p))
    if len(candidates) == 0:
        break
    candidates.sort(key=lambda x:(-x[0], -x[1], -x[2], -x[3]))
    if candidates[0][0] < 2:
        break
    cnt = 0
    for pos in candidates[0][4]:
        cnt += 1
        board[pos[0]][pos[1]] = -2
    score += cnt ** 2

    board = gravity(board)
    board = rotate_90(board)
    board = rotate_90(board)
    board = rotate_90(board)
    board = gravity(board)

    copied = deepcopy(board)

print(score)
