n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

arr = []


def conquer(x, y, n):
    global arr
    num = board[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != board[i][j]:
                conquer(x, y, n // 3)
                conquer(x, y + n // 3, n // 3)
                conquer(x, y + 2 * (n // 3), n // 3)
                conquer(x + n // 3, y, n // 3)
                conquer(x + n // 3, y + n // 3, n // 3)
                conquer(x + n // 3, y + 2 * (n // 3), n // 3)
                conquer(x + 2 * (n // 3), y, n // 3)
                conquer(x + 2 * (n // 3), y + n // 3, n // 3)
                conquer(x + 2 * (n // 3), y + 2 * (n // 3), n // 3)
                return

    arr.append(num)


conquer(0, 0, n)
print(arr.count(-1))
print(arr.count(0))
print(arr.count(1))
