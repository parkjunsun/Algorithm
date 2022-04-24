from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def bfs(start):
    cnt = 0
    q = deque()
    q.append(start)
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1

    return cnt


print(bfs(1))
