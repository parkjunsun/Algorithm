import sys

input = sys.stdin.readline

board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def win_check(x, y, color):
    tmp_x, tmp_y = x, y
    for i in range(4):
        arr = []
        x, y = tmp_x, tmp_y
        arr.append((x, y))
        cnt = 1
        while True:
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < 19 and -1 < ny < 19:
                if board[nx][ny] == color:
                    arr.append((nx, ny))
                    cnt += 1
                else:
                    break
            elif nx <= -1 or nx >= 19 or ny <= -1 or ny >= 19:
                break
            x, y = nx, ny

        x, y = tmp_x, tmp_y
        while True:
            nx = x + dx[i+4]
            ny = y + dy[i+4]
            if -1 < nx < 19 and -1 < ny < 19:
                if board[nx][ny] == color:
                    arr.append((nx, ny))
                    cnt += 1
                else:
                    break
            elif nx <= -1 or nx >= 19 or ny <= -1 or ny >= 19:
                break
            x, y = nx, ny
        if cnt == 5:
            arr.sort(key=lambda x:(x[1], x[0]))
            return True, arr[0][0], arr[0][1]
    return False, -1, -1

b = False
w = False

px, py = 0, 0


for i in range(19):
    for j in range(19):
        if board[i][j] == 1:
            flag, pos_x, pos_y = win_check(i, j, 1)
            if flag:
                px, py = pos_x, pos_y
                b = True
        elif board[i][j] == 2:
            flag2, pos_x, pos_y = win_check(i, j, 2)
            if flag2:
                px, py = pos_x, pos_y
                w = True

if b:
    print(1)
    print(px+1, py+1)
elif w:
    print(2)
    print(px+1, py+1)
else:
    print(0)
