import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

p = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    p[i][1] = board[i-1][0]
    for j in range(1, n+1):
        p[i][j] = p[i][j-1] + board[i-1][j-1]


for i in range(1, n+1):
    for j in range(2, n+1):
        p[j][i] += p[j-1][i]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = p[x2][y2] - p[x1-1][y2] - p[x2][y1-1] + p[x1-1][y1-1]
    print(ans)