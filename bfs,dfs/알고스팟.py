from collections import deque

m, n = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, depth):
    q = deque()
    q.append((x, y, depth))
    visited[x][y] = 1
    while q:
        x, y, depth = q.popleft()
        if x == n-1 and y == m-1:
            return depth
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if visited[nx][ny] == 0:
                    if board[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.appendleft((nx, ny, depth))
                    else:
                        visited[nx][ny] = 1
                        q.append((nx, ny, depth+1))

print(bfs(0,0,0))
