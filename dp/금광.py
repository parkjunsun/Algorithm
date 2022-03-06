t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    arr = list(map(int, input().split()))

    for i in range(n):
        for j in range(m):
            board[i][j] = arr[i*4+j]

    def rotate_90_degree():
        row = len(board)
        col = len(board[0])
        res = [[0] * n for _ in range(m)]
        for r in range(row):
            for c in range(col):
                res[c][row - 1 - r] = board[r][c]
        return res

    mine = rotate_90_degree()

    for i in range(1, m):
        for j in range(n-1):
            if j == 0:
                mine[i][j] += max(mine[i-1][j+1], mine[i-1][j])
            elif j == n-1:
                mine[i][j] += max(mine[i-1][j-1], mine[i-1][j])
            else:
                mine[i][j] += max(mine[i-1][j-1], mine[i-1][j], mine[i-1][j+1])

    print(max(mine[m-1]))