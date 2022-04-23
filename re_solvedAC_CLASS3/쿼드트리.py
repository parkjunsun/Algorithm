n = int(input())

board = []
for _ in range(n):
    board.append(list(map(str, input())))

ans = []


def conquer(x, y, n):
    global ans
    num = board[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != num:
                ans.append('(')
                conquer(x, y, n // 2)
                conquer(x, y + n // 2, n // 2)
                conquer(x + n // 2, y, n // 2)
                conquer(x + n // 2, y + n // 2, n // 2)
                ans.append(')')
                return
    ans.append(num)


conquer(0, 0, n)
print(''.join(ans))
