n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

ans = []


def conquer(x, y, length):
    global ans
    num = board[x][y]

    for i in range(x, x + length):
        for j in range(y, y + length):
            if board[i][j] != num:
                conquer(x, y, length // 2)
                conquer(x, y + length // 2, length // 2)
                conquer(x + length // 2, y, length // 2)
                conquer(x + length // 2, y + length // 2, length // 2)
                return

    ans.append(num)


conquer(0, 0, n)
print(ans.count(0))
print(ans.count(1))
