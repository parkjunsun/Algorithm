from collections import deque
import math
import sys

input = sys.stdin.readline

prime = [0] * 1000001
prime[1] = 1
for i in range(2, int(math.sqrt(1000000)) + 1):
    if prime[i] == 0:
        gop = 2
        while i * gop <= 1000000:
            prime[i*gop] = 1
            gop += 1

def bfs(x, depth):
    q = deque()
    q.append((x, depth))
    visited = [0] * 1000001
    visited[x] = 1
    while q:
        x, depth = q.popleft()
        if prime[x] == 0 and a <= x <= b:
            return depth

        nx = x // 2
        if visited[nx] == 0:
            visited[nx] = 1
            q.append((nx, depth+1))

        nx = x // 3
        if visited[nx] == 0:
            visited[nx] = 1
            q.append((nx, depth + 1))

        if x < b:
            nx = x + 1
            if visited[nx] == 0:
                visited[nx] = 1
                q.append((nx, depth + 1))

        if x > 0:
            nx = x - 1
            if visited[nx] == 0:
                visited[nx] = 1
                q.append((nx, depth + 1))

    return -1

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    print(bfs(n, 0))