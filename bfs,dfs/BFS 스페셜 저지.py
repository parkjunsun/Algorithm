from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n):
    graph[i].sort()

visited = [0] * (n+1)

order = list(map(int, input().split()))
arr = []

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        v = q.popleft()
        arr.append(v)
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

bfs(1)

if arr == order:
    print(1)
else:
    print(0)