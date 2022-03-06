from collections import deque

n, m, t = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
d = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = 1000000
def bfs(x, y):
    global dist
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        if board[x][y] == 2:
            dist = n-1-x + m-1-y + d[x][y]
        if x == n-1 and y == m-1:
            return min(d[x][y], dist)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if board[nx][ny] != 1 and visited[nx][ny] == 0:
                    d[nx][ny] = d[x][y] + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return dist

ans = bfs(0, 0)
print("Fail" if(ans > t) else ans)