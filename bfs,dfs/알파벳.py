n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(str, input())))

alpha = [0] * 26
alpha[ord(board[0][0])-65] = 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_num = 0

def dfs(x, y, depth):
    global max_num
    max_num = max(max_num, depth)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < n and -1 < ny < m:
            if alpha[ord(board[nx][ny])-65] == 0:
                alpha[ord(board[nx][ny])-65] = 1
                print(board[nx][ny])
                dfs(nx, ny, depth+1)
                print("언제")
                alpha[ord(board[nx][ny]) - 65] = 0

dfs(0, 0, 1)
print(max_num)