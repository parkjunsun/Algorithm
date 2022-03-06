from collections import deque

n, k = map(int, input().split())
visited = [0] * (100000+5)

def bfs(x, depth):
    q = deque()
    q.append((x, depth))
    visited[x] = 1

    while q:
        x, depth = q.popleft()
        if x == k:
            return depth
        for nx in (x-1, x+1, 2*x):
            if -1 < nx < 100005:
                if visited[nx] == 0:
                    visited[nx] = 1
                    q.append((nx, depth+1))

print(bfs(n, 0))