from collections import deque


def bfs(x, cmd):
    q = deque()
    visited = [0] * 10001
    q.append((x, cmd))
    visited[x] = 1

    while q:
        x, cmd = q.popleft()
        if x == b:
            return cmd

        nx = (2 * x) % 10000
        if visited[nx] == 0:
            q.append((nx, cmd + "D"))
            visited[nx] = 1

        if x == 0:
            nx = 9999
        else:
            nx = x - 1
        if visited[nx] == 0:
            q.append((nx, cmd + "S"))
            visited[nx] = 1

        nx = (x % 1000) * 10 + (x // 1000)
        if visited[nx] == 0:
            q.append((nx, cmd + "L"))
            visited[nx] = 1

        nx = (x % 10) * 1000 + (x // 10)
        if visited[nx] == 0:
            q.append((nx, cmd + "R"))
            visited[nx] = 1


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, ""))
