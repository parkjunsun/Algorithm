from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]


for i in range(n):
    row = list(map(int, input().split()))
    for j in range(1, len(row)-1, 2):
        graph[row[0]].append([row[j], row[j+1]])

print(graph)

def bfs(start):
    visited = [0] * (n+1)
    dist = [0] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i[0]] == 0:
                visited[i[0]] = 1
                q.append(i[0])
                dist[i[0]] = dist[v] + i[1]
    max_dist = max(dist)
    idx = dist.index(max_dist)
    return idx, max_dist

idx, d = bfs(1)
idx2, answer = bfs(idx)
print(answer)