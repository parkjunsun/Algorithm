from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
num1, num2 = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(v, depth):
    q = deque()
    q.append((v, depth))
    visited[v] = 1
    while q:
        v, depth = q.popleft()
        if v == num2:
            return depth
        for i in graph[v]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, depth+1))
    return -1

print(bfs(num1, 0))