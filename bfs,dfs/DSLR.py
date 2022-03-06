from collections import deque
import sys


def bfs(a, b, empty):
    q = deque()
    q.append((a, empty))
    visited = [0] * 10001
    visited[a] = 1
    while q:
        a, empty = q.popleft()
        if a == b:
            return empty
        na = a * 2
        if na > 9999:
            na = na % 10000
        if visited[na] == 0:
            visited[na] = 1
            q.append((na, empty + 'D'))

        na = a - 1
        if na == -1:
            na = 9999
        if visited[na] == 0:
            visited[na] = 1
            q.append((na, empty + 'S'))

        front = a % 1000
        back = a // 1000
        na = front * 10 + back
        if visited[na] == 0:
            visited[na] = 1
            q.append((na, empty + 'L'))

        front = a % 10
        back = a // 10
        na = front * 1000 + back
        if visited[na] == 0:
            visited[na] = 1
            q.append((na, empty + 'R'))

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b, ''))