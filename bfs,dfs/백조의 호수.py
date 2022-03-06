from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
c = [[0] * m for _ in range(n)]
wc = [[0] * m for _ in range(n)]

board = []
swan = []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(n):
    row = list(map(str, input()))
    board.append(row)
    for j, k in enumerate(row):
        if board[i][j] == 'L':
            swan.append([i, j])
            wq.append([i, j])
        elif board[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan[0][0], swan[0][1], swan[1][0], swan[1][1]
q.append([x1, y1])
board[x1][y1], board[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if not c[nx][ny]:
                    if board[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1

    return 0

def melting():
    while wq:
        x, y = wq.popleft()
        if board[x][y] == 'X':
            board[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m:
                if not wc[nx][ny]:
                    if board[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1


while True:
    melting()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1




