from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

arr = []

def bfs(start, depth):
    q = deque()
    q.append((start, depth))
    visited[start] = 1
    while q:
        v, depth = q.popleft()
        arr.append((v, depth))
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, depth+1))


bfs(1, 0)
arr.sort(key=lambda x:(-x[1], x[0]))
number = arr[0][0]
dist = arr[0][1]
cnt = 1
for i in range(1, len(arr)):
    if arr[i][1] == arr[0][1]:
        cnt += 1
print(number,dist,cnt)
