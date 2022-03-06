import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


flag = 0
def dfs(x, depth):
    global flag
    if depth == 4:
        flag = 1
        return
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i, depth+1)
            visited[i] = 0

for i in range(n):
    visited = [0] * n
    dfs(i, 0)
    if flag == 1:
        print(1)
        sys.exit()

print(0)