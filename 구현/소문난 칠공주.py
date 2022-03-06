from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

board = []
for _ in range(5):
    board.append(list(map(str, input())))

all_pos = []
for i in range(5):
    for j in range(5):
        all_pos.append((i, j, board[i][j]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x,y, value):
    cnt = 1
    S, Y = 0, 0
    visited = [[0] * 5 for _ in range(5)]
    q = deque()
    q.append((x, y))
    if value == 'S':
        S += 1
    else:
        Y += 1
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < 5 and -1 < ny < 5:
                if visited[nx][ny] == 0 and check[nx][ny] != "O":
                    cnt += 1
                    if check[nx][ny] == 'S':
                        S += 1
                    else:
                        Y += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return cnt, S, Y

ans = 0

candidates = list(combinations(all_pos, 7))
for candidate in candidates:
    check = [["O"] * 5 for _ in range(5)]
    sx, sy, sv = 0, 0, ""
    for i in range(len(candidate)):
        sx, sy, sv = candidate[0][0], candidate[0][1], candidate[0][2]
        check[candidate[i][0]][candidate[i][1]] = candidate[i][2]
    count, cnt_s, cnt_y = bfs(sx, sy, sv)
    if count == 7 and cnt_s > cnt_y:
        ans += 1

print(ans)


