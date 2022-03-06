from collections import deque

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]

    for _ in range(k):
        c, r = map(int, input().split())
        board[r][c] = 1

    visited = [[0] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < n and -1 < ny < m:
                    if board[nx][ny] == 1 and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny))


    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)


