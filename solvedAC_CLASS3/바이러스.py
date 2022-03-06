from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                cnt += 1

bfs(1)
print(cnt)
