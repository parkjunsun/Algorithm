from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input())))

visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if visited[nx][ny] == 0:
                    if board[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y]
                        q.appendleft((nx, ny))
                    else:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
bfs(0, 0)
print(visited[-1][-1] - 1)