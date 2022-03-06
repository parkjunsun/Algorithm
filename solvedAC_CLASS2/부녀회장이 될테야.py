t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    board = [[0] * n for _ in range(k+1)]
    for i in range(1, n+1):
        board[0][i-1] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            for x in range(j):
                board[i][j-1] += board[i-1][x]

    print(board[k][n-1])