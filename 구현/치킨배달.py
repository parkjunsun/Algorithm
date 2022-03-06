from itertools import combinations

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
hofs = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            hofs.append((i, j))

cand_hofs = list(combinations(hofs, m))

def init(pos):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                res[i][j] = 1
    for p in pos:
        res[p[0]][p[1]] = 2
    return res

min_total_dist = int(1e9)

for pos in cand_hofs:
    pivot = init(pos)
    chicken_stores = []
    houses = []
    total_dist = 0
    for i in range(n):
        for j in range(n):
            if pivot[i][j] == 1:
                houses.append((i, j))
            if pivot[i][j] == 2:
                chicken_stores.append((i, j))
    for i in range(len(houses)):
        min_dist = int(1e9)
        for j in range(len(chicken_stores)):
            dist = abs(houses[i][0] - chicken_stores[j][0]) + abs(houses[i][1] - chicken_stores[j][1])
            min_dist = min(min_dist, dist)
        total_dist += min_dist
    min_total_dist = min(min_total_dist, total_dist)

print(min_total_dist)


