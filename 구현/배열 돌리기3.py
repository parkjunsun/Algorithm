from copy import deepcopy

n, m, r = map(int, input().split())
board = []
ops = []
for _ in range(n):
    board.append(list(map(int, input().split())))
ops = list(map(int, input().split()))


def calc1(board):
    r = len(board)
    c = len(board[0])
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            res[(r-1) - i][j] = board[i][j]
    return res

def calc2(board):
    r = len(board)
    c = len(board[0])
    res = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            res[i][(c-1) - j] = board[i][j]
    return res

def calc3(board):
    row = len(board)
    column = len(board[0])
    res = [[0] * row for _ in range(column)]
    for r in range(row):
        for c in range(column):
            res[c][row-1-r] = board[r][c]
    return res

def calc4(board):
    row = len(board)
    column = len(board[0])
    res = [[0] * row for _ in range(column)]
    for r in range(row):
        for c in range(column):
            res[column-1-c][r] = board[r][c]
    return res

def calc5(board):
    r = len(board)
    c = len(board[0])
    res = [[0] * c for _ in range(r)]

    for i in range(r//2):
        for j in range(c//2):
            res[i][c//2+j] = board[i][j]

    for i in range(r//2):
        for j in range(c//2, c):
            res[r//2+i][j] = board[i][j]

    for i in range(r//2, r):
        for j in range(c//2):
            res[i-r//2][j] = board[i][j]

    for i in range(r//2, r):
        for j in range(c//2, c):
            res[i][j-c//2] = board[i][j]

    return res

def calc6(board):
    r = len(board)
    c = len(board[0])
    res = [[0] * c for _ in range(r)]

    for i in range(r//2):
        for j in range(c//2):
            res[i+r//2][j] = board[i][j]

    for i in range(r//2):
        for j in range(c//2, c):
            res[i][j-c//2] = board[i][j]

    for i in range(r//2, r):
        for j in range(c//2):
            res[i][j+c//2] = board[i][j]

    for i in range(r//2, r):
        for j in range(c//2, c):
            res[i-r//2][j] = board[i][j]

    return res

for op in ops:
    if op == 1:
        result = calc1(board)
        board = deepcopy(result)
    elif op == 2:
        result = calc2(board)
        board = deepcopy(result)
    elif op == 3:
        result = calc3(board)
        board = deepcopy(result)
    elif op == 4:
        result = calc4(board)
        board = deepcopy(result)
    elif op == 5:
        result = calc5(board)
        board = deepcopy(result)
    elif op == 6:
        result = calc6(board)
        board = deepcopy(result)

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end=' ')
    print()