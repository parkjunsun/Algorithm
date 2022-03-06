from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [0] * (n+1)
visited2 = [0] * (n+1)
def dfs(x):
    visited[x] = 1
    print(x, end=' ')

    for i in graph[x]:
        if visited[i] == 0:
            dfs(i)

def bfs(x):
    q = deque()
    q.append(x)
    visited2[x] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited2[i] == 0:
                visited2[i] = 1
                q.append(i)
dfs(start)
print()
bfs(start)

