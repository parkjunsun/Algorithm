n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

case1 = 0
case2 = 0
case3 = 0
case4 = 0

for i in range(n):
    sums = board[i][0]
    for j in range(m-1):
        if board[i][j] - board[i][j+1] <= 0:
            sums += abs(board[i][j] - board[i][j+1])
    case1 += sums

for i in range(m):
    sums = board[0][i]
    for j in range(n-1):
        if board[j][i] - board[j+1][i] <= 0:
            sums += abs(board[j][i] - board[j+1][i])
    case2 += sums

for i in range(n):
    sums = board[i][-1]
    for j in range(m-1, 0, -1):
        if board[i][j] - board[i][j-1] <= 0:
            sums += abs(board[i][j] - board[i][j-1])
    case3 += sums

for i in range(m):
    sums = board[-1][i]
    for j in range(n-1, 0, -1):
        if board[j][i] - board[j-1][i] <= 0:
            sums += abs(board[j][i] - board[j-1][i])
    case4 += sums

ans = case1 + case2 + case3 + case4 + (n*m)*2
print(ans)





