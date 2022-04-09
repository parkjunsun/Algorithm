from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def dfs(x):
    visited1[x] = 1
    print(x, end=' ')
    for item in graph[x]:
        if visited1[item] == 0:
            dfs(item)


def bfs(x):
    q = deque()
    q.append(x)
    visited2[x] = 1

    while q:
        x = q.popleft()
        print(x, end=' ')
        for item in graph[x]:
            if visited2[item] == 0:
                q.append(item)
                visited2[item] = 1


dfs(v)
print()
bfs(v)
