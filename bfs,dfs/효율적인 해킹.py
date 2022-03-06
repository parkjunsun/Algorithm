from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    cnt = 0
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                cnt += 1
                q.append(i)
    return start, cnt

save = []
for i in range(1, n+1):
    visited = [0] * (n + 1)
    s, c = bfs(i)
    save.append((s, c))

save.sort(key=lambda x:(-x[1], x[0]))
pivot = save[0][1]

for i in range(len(save)):
    if save[i][1] == pivot:
        print(save[i][0], end=' ')
