n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input())))

case1 = [[""] * 8 for _ in range(8)]
case2 = [[""] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                case1[i][j] = 'W'
                case2[i][j] = 'B'
            else:
                case1[i][j] = 'B'
                case2[i][j] = 'W'
        else:
            if j % 2 == 0:
                case1[i][j] = 'B'
                case2[i][j] = 'W'
            else:
                case1[i][j] = 'W'
                case2[i][j] = 'B'


min_cnt1, min_cnt2 = int(1e9), int(1e9)
for i in range(n-8+1):
    for j in range(m-8+1):
        cnt1, cnt2 = 0, 0
        for x in range(8):
            for y in range(8):
                if board[x+i][y+j] != case1[x][y]:
                    cnt1 += 1
                if board[x+i][y+j] != case2[x][y]:
                    cnt2 += 1
        min_cnt1 = min(min_cnt1, cnt1)
        min_cnt2 = min(min_cnt2, cnt2)

print(min(min_cnt1, min_cnt2))