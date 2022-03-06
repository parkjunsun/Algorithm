from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
board = []
arr = []
time = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(n):
        if board[i][j] != 0:
            arr.append((board[i][j], time, i, j))
arr.sort()
s, x, y = map(int, input().split())

visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        v, t, x, y = q.popleft()
        if t == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    board[nx][ny] = v
                    q.append((v, t+1, nx, ny))
                    visited[nx][ny] = 1

q = deque(arr)
bfs()

print(board[x-1][y-1])

