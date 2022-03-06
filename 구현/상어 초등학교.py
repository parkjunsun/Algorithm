import sys

input = sys.stdin.readline

n = int(input())
all = []
board = [[-1] * (n+2) for _ in range(n+2)]
for i in range(1, n+1):
    for j in range(1, n+1):
        board[i][j] = 0
a, b, c, d, e = map(int, input().split())
all.append((a, b, c, d, e))
board[2][2] = a
for _ in range((n**2) - 1):
    empty_pos = []
    candidates = []
    num, n1, n2, n3, n4 = map(int, input().split())
    all.append((num, n1, n2, n3, n4))
    arr = [n1, n2, n3, n4]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] == 0:
                empty_pos.append((i, j))
    for pos in empty_pos:
        cnt1 = 0
        cnt2 = 0
        x, y = pos[0], pos[1]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if board[x+dx][y+dy] in arr:
                cnt1 += 1
            elif board[x+dx][y+dy] == 0:
                cnt2 += 1
        candidates.append((x, y, cnt1, cnt2))
    candidates.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
    c1, c2 = candidates[0][0], candidates[0][1]
    board[c1][c2] = num

total = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        score = 0
        for k in all:
            if board[i][j] == k[0]:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if board[i+dx][j+dy] in k:
                        score += 1
        if score == 0:
            satisfy = 0
        elif score == 1:
            satisfy = 1
        elif score == 2:
            satisfy = 10
        elif score == 3:
            satisfy = 100
        else:
            satisfy = 1000
        total += satisfy

print(total)