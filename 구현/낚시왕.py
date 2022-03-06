import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[[0] * 3 for _ in range(C)] for _ in range(R)]
answer = 0
total = C

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def moving():
    pos = []
    for i in range(R):
        for j in range(C):
            if board[i][j][1] != 0:
                x, y = i, j
                move = board[i][j][0]
                direction = board[i][j][1]
                size = board[i][j][2]
                board[i][j][0] = 0
                board[i][j][1] = 0
                board[i][j][2] = 0
                for k in range(move):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if nx == -1:
                        nx = 1
                        direction = 2
                    if nx == R:
                        nx = R - 2
                        direction = 1
                    if ny == -1:
                        ny = 1
                        direction = 3
                    if ny == C:
                        ny = C - 2
                        direction = 4
                    x, y = nx, ny
                pos.append((x, y, move, direction, size))
    pos.sort(key=lambda x:(x[4]))
    for fish in pos:
        x_pos, y_pos = fish[0], fish[1]
        move = fish[2]
        direction = fish[3]
        size = fish[4]
        board[x_pos][y_pos][0] = move
        board[x_pos][y_pos][1] = direction
        board[x_pos][y_pos][2] = size

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1][0] = s
    board[r-1][c-1][1] = d
    board[r-1][c-1][2] = z

for walk in range(total):
    zones = []
    for i in range(C):
        tmp = []
        for j in range(R):
            tmp.append(board[j][i])
        zones.append(tmp)
    for i in range(len(zones[walk])):
        if zones[walk][i][1] != 0:
            answer += zones[walk][i][2]
            board[i][walk][0] = 0
            board[i][walk][1] = 0
            board[i][walk][2] = 0
            break
    moving()

print(answer)