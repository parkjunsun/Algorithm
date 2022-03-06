n, m, r = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

top, left, bottom, right = 0, 0, n - 1, m - 1
while True:
    if top > bottom or left > right:
        break
    for _ in range(r):
        tmp = board[top][right]
        for i in range(top, bottom):
            board[i][right] = board[i+1][right]
        for i in range(right, left, -1):
            board[bottom][i] = board[bottom][i-1]
        for i in range(bottom, top, -1):
            board[i][left] = board[i-1][left]
        for i in range(left, right):
            board[top][i] = board[top][i+1]
        board[top][right-1] = tmp
    top += 1
    left += 1
    bottom -= 1
    right -= 1

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()