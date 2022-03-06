n, m, k = map(int, input().split())
food = [[5] * n for _ in range(n)]
add_feed = []
tree = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(n):
    add_feed.append(list(map(int, input().split())))


for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


for _ in range(k):
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) == 0:
                continue
            tree[i][j].sort()
            idx = 0
            while idx < len(tree[i][j]):
                if tree[i][j][idx] <= food[i][j]:
                    food[i][j] -= tree[i][j][idx]
                    tree[i][j][idx] += 1
                    idx += 1
                else:
                    die_tree = tree[i][j][idx:]
                    for dtree in die_tree:
                        food[i][j] += dtree // 2
                    tree[i][j] = tree[i][j][:idx]
                    break
    for i in range(n):
        for j in range(n):
            c = 0
            if tree[i][j]:
                for old in tree[i][j]:
                    if old % 5 == 0:
                        c += 1
            if c > 0:
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if -1 < nx < n and -1 < ny < n:
                        for _ in range(c):
                            tree[nx][ny].append(1)

    for i in range(n):
        for j in range(n):
            food[i][j] += add_feed[i][j]

answer = 0

for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer)

