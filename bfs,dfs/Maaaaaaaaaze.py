from collections import deque
from itertools import permutations
from copy import deepcopy
import sys

input = sys.stdin.readline

def rotate_90(panel, num):
    res = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            res[j][5-i-1] = panel[i][j]

    for i in range(5):
        for j in range(5):
            board[num][i][j] = res[i][j]

board = []
for _ in range(5):
    tmp = []
    for _ in range(5):
        tmp.append(list(map(int, input().split())))
    board.append(tmp)

tmp = deepcopy(board)

dz = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

def bfs(z, x, y, depth):
    q = deque()
    q.append((z, x, y, depth))
    visited = [[[0] * 5 for _ in range(5)] for _ in range(5)]
    visited[z][x][y] = 1
    while q:
        z, x, y, depth = q.popleft()
        if z == 4 and x == 4 and y == 4:
            return depth
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nz < 5 and -1 < nx < 5 and -1 < ny < 5:
                if board[nz][nx][ny] == 1 and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = 1
                    q.append((nz, nx, ny, depth + 1))
    return -1

checked = []
min_num = int(1e9)

idx = [0, 1, 2, 3, 4]
candidates = list(permutations(idx, 5))

for i in range(len(candidates)):
    for j in range(5):
        board[j] = tmp[candidates[i][j]]
    for _ in range(4):
        rotate_90(board[0], 0)
        for _ in range(4):
            rotate_90(board[1], 1)
            for _ in range(4):
                rotate_90(board[2], 2)
                for _ in range(4):
                    rotate_90(board[3], 3)
                    for _ in range(4):
                        rotate_90(board[4], 4)
                        if board[0][0][0] == 0 or board[4][4][4] == 0:
                            continue

                        result = bfs(0, 0, 0, 0)
                        if result == 12:
                            print(12)
                            sys.exit()
                        if result != -1:
                            min_num = min(min_num, result)


if min_num == int(1e9):
    print(-1)
else:
    print(min_num)

