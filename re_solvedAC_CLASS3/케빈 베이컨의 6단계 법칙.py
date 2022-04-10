from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()


def bfs(start, end, depth):
    q = deque()
    visited = [0] * (n+1)
    q.append((start, depth))
    visited[start] = 1

    while q:
        x, depth = q.popleft()
        if x == end:
            return depth
        for item in graph[x]:
            if visited[item] == 0:
                q.append((item, depth+1))
                visited[item] = 1


for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if i == j:
            continue
        cnt += bfs(i, j, 0)
    arr.append((i, cnt))

arr.sort(key=lambda x: (x[1], x[0]))
print(arr[0][0])



