from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

answer = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)