n = int(input())
board = []
for _ in range(n):
    arr = list(map(int, input().split()))
    board.append(arr)

for i in range(1, n):
    for j in range(len(board[i])):
        if j == 0:
            board[i][j] += board[i-1][j]
        elif j == len(board[i]) - 1:
            board[i][j] += board[i-1][j-1]
        else:
            board[i][j] += max(board[i-1][j-1], board[i-1][j])

print(max(board[n-1]))
