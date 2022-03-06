from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

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
    node = dist.index(max_dist)

    return node, max_dist

node, dist = bfs(1)
node2, answer = bfs(node)

print(answer)