from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    cnt += 1
    return cnt

arr = []
total = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j] == 0:
            arr.append(bfs(i, j))
            total += 1

arr.sort()

print(total)
for item in arr:
    print(item)