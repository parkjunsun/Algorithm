from collections import deque

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input())))
visited = []

dx = [(-1, -1, -1), (1, 1, 1), (0, 0, 0), (0, 0, 0)]
dy = [(0, 0, 0), (0, 0, 0), (-1, -1, -1), (1, 1, 1)]

b_pos = []
e_pos = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 'B':
            b_pos.append((i, j))
        elif board[i][j] == 'E':
            e_pos.append((i, j))



def bfs(b_pos, depth):
    q = deque()
    q.append((b_pos, depth))
    visited.append(b_pos)
    while q:
        b, depth = q.popleft()
        if b == e_pos:
            return depth
        for i in range(4):
            nx1, nx2, nx3 = b[0][0] + dx[i][0], b[1][0] + dx[i][1], b[2][0] + dx[i][2]
            ny1, ny2, ny3 = b[0][1] + dy[i][0], b[1][1] + dy[i][1], b[2][1] + dy[i][2]
            if -1 < nx1 < n and -1 < nx2 < n and -1 < nx3 < n and -1 < ny1 < n and -1 < ny2 < n and -1 < ny3 < n:
                if board[nx1][ny1] != '1' and board[nx2][ny2] != '1' and board[nx3][ny3] != '1' and [(nx1, ny1), (nx2, ny2), (nx3, ny3)] not in visited:
                    q.append(([(nx1, ny1), (nx2, ny2), (nx3, ny3)], depth + 1))
                    visited.append([(nx1, ny1), (nx2, ny2), (nx3, ny3)])

        if b[0][0] == b[1][0] and b[0][0] == b[2][0] and b[1][0] == b[2][0]:
            if b[0][0] == 0 or b[0][0] == n-1:
                continue
            if board[b[0][0]-1][b[0][1]] == '1' or board[b[1][0]-1][b[1][1]] == '1' or board[b[2][0]-1][b[2][1]] == '1':
                continue
            if board[b[0][0]+1][b[0][1]] == '1' or board[b[1][0]+1][b[1][1]] == '1' or board[b[2][0]+1][b[2][1]] == '1':
                continue
            nx1, nx2, nx3 = b[1][0]-1, b[1][0], b[1][0]+1
            ny1, ny2, ny3 = b[1][1], b[1][1], b[1][1]

            if [(nx1, ny1), (nx2, ny2), (nx3, ny3)] not in visited:
                q.append(([(nx1, ny1), (nx2, ny2), (nx3, ny3)], depth + 1))
                visited.append([(nx1, ny1), (nx2, ny2), (nx3, ny3)])
        elif b[0][1] == b[1][1] and b[0][1] == b[2][1] and b[1][1] == b[2][1]:
            if b[0][1] == 0 or b[0][1] == n-1:
                continue
            if board[b[0][0]][b[0][1]-1] == '1' or board[b[1][0]][b[1][1]-1] == '1' or board[b[2][0]][b[2][1]-1] == '1':
                continue
            if board[b[0][0]][b[0][1]+1] == '1' or board[b[1][0]][b[1][1]+1] == '1' or board[b[2][0]][b[2][1]+1] == '1':
                continue
            nx1, nx2, nx3 = b[1][0], b[1][0], b[1][0]
            ny1, ny2, ny3 = b[1][1]-1, b[1][1], b[1][1]+1

            if [(nx1, ny1), (nx2, ny2), (nx3,ny3)] not in visited:
                q.append(([(nx1, ny1), (nx2, ny2), (nx3, ny3)], depth + 1))
                visited.append([(nx1, ny1), (nx2, ny2), (nx3, ny3)])
    return 0

print(bfs(b_pos, 0))


