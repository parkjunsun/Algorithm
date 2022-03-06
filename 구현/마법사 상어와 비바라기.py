import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

init_pos = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    tmp = []
    d, s = map(int, input().split())
    for pos in init_pos:
        x, y = pos[0], pos[1]
        for i in range(s):
            nx = x + dx[d - 1]
            ny = y + dy[d - 1]
            if nx == -1:
                nx = n - 1
            if nx == n:
                nx = 0
            if ny == -1:
                ny = n - 1
            if ny == n:
                ny = 0
            x, y = nx, ny
        tmp.append((nx, ny))
        board[nx][ny] += 1
    for pos in tmp:
        cnt = 0
        nx, ny = pos[0], pos[1]
        if -1 < nx - 1 < n and -1 < ny - 1 < n:
            if board[nx - 1][ny - 1] > 0:
                cnt += 1
        if -1 < nx + 1 < n and -1 < ny - 1 < n:
            if board[nx + 1][ny - 1] > 0:
                cnt += 1
        if -1 < nx - 1 < n and -1 < ny + 1 < n:
            if board[nx - 1][ny + 1] > 0:
                cnt += 1
        if -1 < nx + 1 < n and -1 < ny + 1 < n:
            if board[nx + 1][ny + 1] > 0:
                cnt += 1
        board[nx][ny] += cnt

    init_pos.clear()

    for r in range(n):
        for c in range(n):
            if board[r][c] >= 2:
                init_pos.append((r, c))

    for p in tmp:
        if p in init_pos:
            init_pos.remove(p)

    for pos in init_pos:
        if board[pos[0]][pos[1]] >= 2:
            board[pos[0]][pos[1]] -= 2

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]

print(answer)



