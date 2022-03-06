from collections import deque
import sys

input = sys.stdin.readline

board = []
for _ in range(8):
    board.append(list(map(str, input())))


dx = [0, -1, -1, -1, 0, 1, 1, 1, 0]
dy = [0, -1, 0, 1, 1, 1, 0, -1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        walls = []
        visited = [[0] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if board[i][j] == '#':
                    walls.append((i, j))
        walls.sort(key=lambda x: (-x[0], -x[1]))
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == 0 and y == 7:
                return 1
            if board[x][y] == '#':
                continue
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < 8 and -1 < ny < 8:
                    if board[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))
        for wall in walls:
            board[wall[0]][wall[1]] = '.'
            nr = wall[0] + 1
            nc = wall[1]
            if nr == 8:
                continue
            board[nr][nc] = '#'
    return 0
print(bfs(7, 0))