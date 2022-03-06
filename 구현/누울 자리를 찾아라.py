n = int(input())
board = []
for _ in range(n):
    board.append(list(map(str, input())))

w = []
h = []

for i in range(n):
    w.append(board[i])

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(board[j][i])
    h.append(tmp)


def count(arr):
    total = 0
    for item in arr:
        space = 0
        possible = 0
        for i in range(n):
            if item[i] == '.':
                space += 1
            elif item[i] == 'X':
                if space >= 2:
                    possible += 1
                space = 0
        if space >= 2:
            possible += 1
        total += possible
    return total

print(count(w), count(h))

