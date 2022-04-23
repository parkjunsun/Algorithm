from collections import deque

n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, depth):
    q = deque()
    visited = [[0] * m for _ in range(n)]
    q.append((x, y, depth))
    visited[x][y] = 1

    while q:
        x, y, depth = q.popleft()
        if x == n - 1 and y == m - 1:
            return depth

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny, depth + 1))
                    visited[nx][ny] = 1


print(bfs(0, 0, 1))
