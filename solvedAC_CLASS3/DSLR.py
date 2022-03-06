from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    op = ""
    q = deque()
    visited = [0] * 10001
    q.append((a, op))
    visited[a] = 1

    while q:
        a, op = q.popleft()
        if a == b:
            print(op)

        na = (2 * a) % 10000
        if visited[na] == 0:
            q.append((na, op+'D'))
            visited[na] = 1

        na = a - 1
        if a == 0:
            na = 9999
        if visited[na] == 0:
            q.append((na, op+'S'))
            visited[na] = 1

        front = a // 1000
        remain = a % 1000
        na = remain * 10 + front
        if visited[na] == 0:
            q.append((na, op+'L'))
            visited[na] = 1

        back = a % 10
        remain = a // 10
        na = back * 1000 + remain
        if visited[na] == 0:
            q.append((na, op+'R'))
            visited[na] = 1




