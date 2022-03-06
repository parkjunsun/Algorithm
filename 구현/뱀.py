n = int(input())
board = [[0] * n for _ in range(n)]
k = int(input())
for i in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 5

cmds = []
l = int(input())

for i in range(l):
    t, d = map(str, input().split())
    cmds.append((int(t), d))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
board[x][y] = 1
direction = 1

visited = [(x,y)]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

time = 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx >= n or nx <= -1 or ny >= n or ny <= -1:
        break
    visited.append((nx, ny))
    if board[nx][ny] == 5:
        board[nx][ny] = 1
    elif board[nx][ny] == 0:
        rx, ry = visited.pop(0)
        board[rx][ry] = 0
        board[nx][ny] = 1
    elif board[nx][ny] == 1:
        break
    for cmd in cmds:
        if time == cmd[0]:
            if cmd[1] == 'L':
                turn_left()
            else:
                turn_right()
            cmds.remove(cmd)
    x, y = nx, ny

print(time)