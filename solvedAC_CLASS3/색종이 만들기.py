n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = []

def cal(x, y, n):
    global result
    num = board[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != board[i][j]:
                cal(x, y, n//2)
                cal(x, y+n//2, n//2)
                cal(x+n//2, y, n//2)
                cal(x+n//2, y+n//2, n//2)
                return

    result.append(num)

cal(0, 0, n)

print(result.count(0))
print(result.count(1))