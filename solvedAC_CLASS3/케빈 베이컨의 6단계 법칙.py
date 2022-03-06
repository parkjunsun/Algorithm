from collections import deque

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

candidates = []
for i in range(1, n+1):
    candidates.append((i, sum(graph[i])))

candidates.sort(key=lambda x:(x[1], x[0]))
print(candidates[0][0])

# graph = [[] for _ in range(n+1)]
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
#
# def bfs(x, goal, depth):
#     q = deque()
#     visited = [0] * (n+1)
#     q.append((x, depth))
#     visited[x] = 1
#
#     while q:
#         v, depth = q.popleft()
#         if v == goal:
#             return depth
#         for i in graph[v]:
#             if not visited[i]:
#                 q.append((i, depth+1))
#                 visited[i] = 1
#
# candidates = []
# for i in range(1, n+1):
#     total = 0
#     for j in range(1, n+1):
#         if i == j:
#             continue
#         total += bfs(i, j, 0)
#     candidates.append((i, total))
#
# candidates.sort(key=lambda x:(x[1], x[0]))
# print(candidates[0][0])
