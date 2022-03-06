from collections import deque

m, n = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
check_cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j, 0))
            visited[i][j] = 1
        if board[i][j] == 0:
            check_cnt += 1

already = False
not_able = False
if check_cnt == 0:
    already = True


def check():
    global not_able

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                not_able = True

while q:
    x, y, depth = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < n and -1 < ny < m:
            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                board[nx][ny] = 1
                q.append((nx, ny, depth+1))

check()

if already:
    print(0)
elif not_able:
    print(-1)
else:
    print(depth)
