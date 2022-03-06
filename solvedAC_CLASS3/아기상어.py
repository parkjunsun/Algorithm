from collections import deque

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sx, sy = i, j

size = 2
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, depth):
    eats = []
    q = deque()
    visited = [[0] * n for _ in range(n)]
    q.append((x, y, depth))
    visited[x][y] = 1

    while q:
        x, y, depth = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if visited[nx][ny] == 0:
                    if board[nx][ny] == size or board[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, depth+1))
                    elif board[nx][ny] < size and board[nx][ny] != 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, depth+1))
                        eats.append((nx, ny, board[nx][ny], depth+1))

    return eats


ans = 0
eat_cnt = 0
while True:

    outs = bfs(sx, sy, 0)
    board[sx][sy] = 0
    if len(outs) == 0:
        break
    outs.sort(key=lambda x:(x[3], x[0], x[1]))
    sx, sy, eat_size, time = outs[0][0], outs[0][1], outs[0][2], outs[0][3]
    board[sx][sy] = 9
    ans += time
    eat_cnt += 1

    if eat_cnt == size:
        size += 1
        eat_cnt = 0

print(ans)


