from itertools import permutations
from copy import deepcopy

n, m, r = map(int, input().split())
board = []
ops = []
for _ in range(n):
    board.append(list(map(int, input().split())))

save = deepcopy(board)

for _ in range(r):
    r, c, s = map(int, input().split())
    ops.append((r, c, s))

candidates = list(permutations(ops))

def rotate_clockwise(r, c ,s):
    top = r - s - 1
    left = c - s - 1
    bottom = r + s - 1
    right = c + s - 1

    while True:
        if top >= bottom or left >= right:
            break

        tmp = board[top][left]
        for i in range(top, bottom):
            board[i][left] = board[i+1][left]
        for i in range(left, right):
            board[bottom][i] = board[bottom][i+1]
        for i in range(bottom, top, -1):
            board[i][right] = board[i-1][right]
        for i in range(right, left, -1):
            board[top][i] = board[top][i-1]
        board[top][left+1] = tmp

        top += 1
        left += 1
        bottom -= 1
        right -= 1

def check():
    res = int(1e9)
    for i in range(n):
        res = min(res, sum(board[i]))
    return res

ans = int(1e9)

for candidate in candidates:
    board = deepcopy(save)
    for op in candidate:
        r, c, s = op[0], op[1], op[2]
        rotate_clockwise(r, c, s)
    v = check()
    ans = min(ans, v)

print(ans)

