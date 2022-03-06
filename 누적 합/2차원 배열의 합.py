import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

p = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    p[i][1] = board[i-1][0]
    for j in range(2, m+1):
        p[i][j] = p[i][j-1] + board[i-1][j-1]


for i in range(1, m+1):
    for j in range(1, n+1):
        p[j][i] += p[j-1][i]

t = int(input())
for _ in range(t):
    sx, sy, dx, dy = map(int, input().split())
    ans = p[dx][dy] - p[sx-1][dy] - p[dx][sy-1] + p[sx-1][sy-1]
    print(ans)