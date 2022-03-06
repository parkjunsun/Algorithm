from collections import deque

n, q = map(int, input().split())
board = []
for _ in range(2**n):
    board.append(list(map(int, input().split())))
ls = list(map(int, input().split()))
ls.reverse()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
size = []

def rotate_90(board):
    x = len(board)
    y = len(board[0])

    res = [[0] * y for _ in range(x)]
    for r in range(x):
        for c in range(y):
            res[c][x-r-1] = board[r][c]

    return res

def cut(x, y, board):
    res = [[0] * 2**l for _ in range(2**l)]
    for i in range(x, x+2**l):
        for j in range(y, y+2**l):
            res[i-x][j-y] = board[i][j]
    return res

def filling(sub):
    global add1, add2
    x = len(sub)
    y = len(sub[0])

    for i in range(x):
        for j in range(y):
            box[i+add1][j+add2] = sub[i][j]
    add2 += 2 ** l
    if add2 >= 2 ** n:
        add1 += 2 ** l
        add2 = 0
    if add1 >= 2 ** n:
        add1 = 0

def find_ice(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if box[nx][ny] <= 0:
            cnt += 1
    if cnt >= 2:
        candidates.append((x, y))

def bfs(x, y):
    cnt = 1
    q = deque()
    visited = [[0] * (2**n) for _ in range(2**n)]
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < 2**n and -1 < ny < 2**n:
                if board[nx][ny] > 0 and visited[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    size.append(cnt)

def padding(b):
    res = [[0] * (2**n + 2) for _ in range(2**n + 2)]
    for i in range(len(b)):
        for j in range(len(b[0])):
            res[1+i][1+j] = b[i][j]
    return res

for _ in range(q):
    l = ls.pop()
    candidates = []
    add1 = 0
    add2 = 0
    box = [[0] * 2**n for _ in range(2**n)]

    for i in range(0, 2**n, 2**l):
        for j in range(0, 2**n, 2**l):
            sub = cut(i, j, board)
            rsub = rotate_90(sub)
            filling(rsub)

    box = padding(box)

    for i in range(1, len(box)-1):
        for j in range(1, len(box[0])-1):
            if box[i][j] > 0:
                find_ice(i, j)

    for pos in candidates:
        box[pos[0]][pos[1]] -= 1


    board = [[0] * 2**n for _ in range(2**n)]
    for i in range(1, len(box)-1):
        for j in range(1, len(box[0])-1):
            board[i-1][j-1] = box[i][j]

ice_sum = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        ice_sum += board[i][j]
        if board[i][j] != 0:
            bfs(i, j)

if len(size) == 0:
    print(ice_sum, 0)
else:
    print(ice_sum, max(size))
