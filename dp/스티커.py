import sys

def rotate_90(board):
    r = len(board)
    c = len(board[0])

    res = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            res[j][r - i - 1] = board[i][j]

    return res


t = int(input())
for _ in range(t):
    n = int(input())

    board = []
    for _ in range(2):
        board.append(list(map(int, input().split())))

    if n == 1:
        print(max(board[0][0], board[1][0]))
        continue

    res = rotate_90(board)

    res[1][0] += res[0][1]
    res[1][1] += res[0][0]

    for i in range(2, n):
        for j in range(2):
            if j == 0:
                res[i][j] += max(res[i-1][1], res[i-2][0], res[i-2][1])
            else:
                res[i][j] += max(res[i-1][0], res[i-2][0], res[i-2][1])

    print(max(res[-1]))