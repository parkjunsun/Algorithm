n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

res = []
for i in range(5):
    tmp = []
    for j in range(n):
        tmp.append(board[j][i])
    res.append(tmp)

idx = []

for k in range(n):
    ans = []
    for i in range(5):
        pivot = res[i][k]
        for j in range(n):
            if pivot == res[i][j]:
                if j not in ans:
                    ans.append(j)
    idx.append((k+1, len(ans)-1))

idx.sort(key=lambda x:(-x[1], x[0]))
print(idx[0][0])