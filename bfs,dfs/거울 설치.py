from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input())))
visited = [[0] * n for _ in range(n)]

mirror_pos = []
door_pos = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '#':
            door_pos.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, cnt, dir):
    q = deque()
    q.append((x, y, cnt, dir))
    visited[x][y] = 1
    while q:
        x, y, cnt, dir = q.popleft()
        if x == fx and y == fy:
            return cnt

        if board[x][y] == '.' or board[x][y] == '#':
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < n and -1 < ny < n:
                    if (board[nx][ny] == '.' or board[nx][ny] == '#') and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt, i))
                    elif board[nx][ny] == '!' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt+1, i))
        elif board[x][y] == '!':
            dir1 = dir - 1
            if dir1 == -1:
                dir1 = 3

            dir2 = dir + 1
            if dir2 == 4:
                dir2 = 0

            for i in [dir1, dir2]:
                nx = x + dx[i]
                ny = y + dy[i]
                if -1 < nx < n and -1 < ny < n:
                    if (board[nx][ny] == '.' or board[nx][ny] == '#') and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt, i))
                    elif board[nx][ny] == '!' and visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt+1, i))


sx, sy = door_pos[0][0], door_pos[0][1]
fx, fy = door_pos[1][0], door_pos[1][1]

print(bfs(sx, sy, 0, 0))

