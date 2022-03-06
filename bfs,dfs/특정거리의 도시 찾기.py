from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
print(graph)
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

arr = []
def bfs(x, depth):
    q = deque()
    q.append((x, depth))
    visited[x] = 1
    while q:
        v, depth = q.popleft()
        if depth == k:
            arr.append(v)
        for i in graph[v]:
            if not visited[i]:
                q.append((i, depth+1))
                visited[i] = 1
    arr.append(-1)

bfs(x, 0)
arr.sort()
if len(arr) != 1:
    for i in range(1, len(arr)):
        print(arr[i])
else:
    print(arr[0])



