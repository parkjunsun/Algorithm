from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001


def bfs(x, depth):
    q = deque()
    q.append((x, depth))
    visited[x] = 1

    while q:
        x, depth = q.popleft()
        if x == k:
            return depth

        for nx in (x - 1, x + 1, 2 * x):
            if -1 < nx < 100001:
                if visited[nx] == 0:
                    q.append((nx, depth + 1))
                    visited[nx] = 1


ans = bfs(n, 0)
print(ans)
