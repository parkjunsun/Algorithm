n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = []

def dq(x, y, n):
    global result
    num = board[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != board[i][j]:
                dq(x, y, n//3)
                dq(x, y+n//3, n//3)
                dq(x, y+2*(n//3), n//3)
                dq(x+n//3, y, n//3)
                dq(x+n//3, y+n//3, n//3)
                dq(x+n//3, y+2*(n//3), n//3)
                dq(x+2*(n//3), y, n//3)
                dq(x+2*(n//3), y+n//3, n//3)
                dq(x+2*(n//3), y+2*(n//3), n//3)
                return

    result.append(num)

dq(0, 0, n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))
