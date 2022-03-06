n, m, b = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

min_time = int(1e9)
height = -1

for h in range(257):
    case1, case2 = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] < h:
                case2 += h - board[i][j]
            else:
                case1 += board[i][j] - h
    if case2 > case1 + b:
        continue
    time = 2 * case1 + case2
    if time <= min_time:
        min_time = time
        height = h

print(min_time, height)


