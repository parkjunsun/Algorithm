t = int(input())

for _ in range(t):
    n = int(input())
    k = int(input())

    r = n + 1
    c = k

    board = [[0] * c for _ in range(r)]

    for i in range(c):
        board[0][i] = i + 1

    for i in range(1, r):
        for j in range(c):
            for z in range(j + 1):
                board[i][j] += board[i - 1][z]

    print(board[n][k - 1])
