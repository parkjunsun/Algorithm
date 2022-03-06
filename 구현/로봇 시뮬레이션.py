import sys

m, n = map(int, input().split())
board = [[[0, 0]] * m for _ in range(n)]

passing = True

a, b = map(int, input().split())
for i in range(a):
    direction = 0
    c, r, di = input().split()
    if di == 'N':
        direction = 0
    elif di == 'E':
        direction = 1
    elif di == 'S':
        direction = 2
    elif di == 'W':
        direction = 3
    board[int(r)-1][int(c)-1] = [i+1, direction]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

command = []

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

def turn_right():
    global d
    d += 1
    if d == 4:
        d = 0

for _ in range(b):
    robot, char, count = map(str, input().split())
    command.append([int(robot), char, int(count)])

for comm in command:
    robot, cmd, count = comm[0], comm[1], comm[2]
    x, y, d = 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j][0] == robot:
                x, y, d = i, j, board[i][j][1]
    if cmd == 'F':
        for c in range(count):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= n or nx <= -1 or ny >= m or ny <= -1:
                print(f"Robot {robot} crashes into the wall")
                passing = False
                sys.exit()
            elif -1 < nx < n and -1 < ny < m:
                if board[nx][ny][0] != 0:
                    print(f"Robot {robot} crashes into robot {board[nx][ny][0]}")
                    passing = False
                    sys.exit()
                else:
                    board[nx][ny] = [robot, d]
                    board[x][y] = [0, 0]
            x, y = nx, ny
    elif cmd == 'L':
        for k in range(count):
            turn_left()
        board[x][y] = [robot, d]
    elif cmd == 'R':
        for k in range(count):
            turn_right()
        board[x][y] = [robot, d]

if passing:
    print("OK")
