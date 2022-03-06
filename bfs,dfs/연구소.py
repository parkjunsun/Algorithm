from itertools import combinations
from copy import deepcopy
from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j))

candidates = list(combinations(empty, 3))

def init(cand):
    copied = deepcopy(board)
    for c in cand:
        copied[c[0]][c[1]] = 1
    return copied

def bfs(x, y, graph):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    graph[nx][ny] = 2
                    visited[nx][ny] = 1
                    q.append((nx, ny))

def find(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt


max_num = 0

for candidate in candidates:
    res = init(candidate)
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if res[i][j] == 2 and visited[i][j] == 0:
                bfs(i, j, res)
    num = find(res)
    max_num = max(max_num, num)

print(max_num)






